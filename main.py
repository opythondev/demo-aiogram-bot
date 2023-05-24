import asyncio
import logging
import asyncpg
from datetime import datetime, timedelta

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram import Bot, Dispatcher, F
from aiogram.types import ContentType
from aiogram.filters import CommandStart, Command

from aiogram.fsm.storage.redis import RedisStorage
from apscheduler.jobstores.redis import RedisJobStore
from apscheduler_di import ContextSchedulerDecorator

from core.handlers.basic import get_start, get_photo, get_hello, get_location, get_inline
from core.handlers.contact import get_fake_contacts, get_true_contacts
from core.handlers.callback import select_macbook
from core.handlers.payments import order, pre_checkout_query, successful_payment, shipping_check
from core.handlers import fsmform
from core.handlers import appscheduler
from core.handlers import sendmedia

from core.filters.iscontact import IsTrueContact
from core.settings import settings

from core.utils.commands import set_commands
from core.utils.callbackdata import MacInfo
from core.utils.statesform import StepsForm

from core.middlewares.countermiddleware import CounterMiddleware
from core.middlewares.officehours import OfficeHoursMiddleware
from core.middlewares.dbmiddleware import DbSession
from core.middlewares.apschedulermiddleware import ApschedulerMiddleware


async def on_start(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, text="Bot был запущен")


async def on_stop(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text="Bot был остановлен")


async def create_pool():
    return await asyncpg.create_pool(user="root", password='example', database='pgtests',
                                     host='127.0.0.1', port=5432, command_timeout=60)


async def start():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(name)s -"
                               " (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")

    bot = Bot(settings.bots.bot_token, parse_mode='HTML')

    connection_pool = await create_pool()

    storage = RedisStorage.from_url("redis://127.0.0.1:6379/0",
                                    connection_kwargs={"password": settings.bots.redis_pass})

    dp = Dispatcher(storage=storage)

    jobstorage = {
        "default": RedisJobStore(
            jobs_key='dispatched_jobs',
            run_times_key='dispatched_running',
            host='127.0.0.1',
            port=6379,
            db=2,
            password=settings.bots.redis_pass
        )
    }

    scheduler = ContextSchedulerDecorator(AsyncIOScheduler(timezone="Europe/Moscow", jobstores=jobstorage))
    scheduler.ctx.add_instance(bot, declared_class=Bot)
    # scheduler.add_job(appscheduler.send_message_time,
    #                   trigger="date", run_date=datetime.now() + timedelta(seconds=10.0))
    # scheduler.add_job(appscheduler.send_message_cron,
    #                   trigger="cron",
    #                   hour=datetime.now().hour, minute=datetime.now().minute + 1,
    #                   start_date=datetime.now())
    # scheduler.add_job(appscheduler.send_message_interval,
    #                   trigger="interval",
    #                   seconds=60)

    scheduler.start()

    dp.startup.register(on_start)
    dp.shutdown.register(on_stop)

    # Middlewares
    """
    Each update(event) will pass through all middlewares
    """
    # Scheduler Middleware
    dp.update.middleware.register(ApschedulerMiddleware(scheduler))
    # Counter middleware
    dp.message.middleware.register(CounterMiddleware())

    # Working hours middleware
    # if event type Message
    # dp.message.middleware.register(OfficeHoursMiddleware())
    # if event type Any Update
    dp.update.middleware.register(OfficeHoursMiddleware())

    # DB middleware
    dp.message.middleware.register(DbSession(connection_pool))

    # Хэндлеры отрабатывают по порядку, сверху вниз
    dp.message.register(sendmedia.get_audio, Command(commands=["audio"]))
    dp.message.register(sendmedia.get_document, Command(commands=["document"]))
    dp.message.register(sendmedia.get_media_group, Command(commands=["mediagroup"]))
    dp.message.register(sendmedia.get_photo, Command(commands=["photo"]))
    dp.message.register(sendmedia.get_sticker, Command(commands=["sticker"]))
    dp.message.register(sendmedia.get_video, Command(commands=["video"]))
    dp.message.register(sendmedia.get_video_note, Command(commands=["video_note"]))
    dp.message.register(sendmedia.get_voice, Command(commands=["voice"]))

    dp.message.register(fsmform.get_form, Command(commands=["form"]))
    dp.message.register(fsmform.get_name, StepsForm.GET_NAME)
    dp.message.register(fsmform.get_last_name, StepsForm.GET_LAST_NAME)
    dp.message.register(fsmform.get_age, StepsForm.GET_AGE)

    dp.message.register(get_inline, Command(commands=["inline"]))

    dp.message.register(order, Command(commands=["pay"]))
    dp.pre_checkout_query.register(pre_checkout_query)
    dp.message.register(successful_payment, F.content_type == ContentType.SUCCESSFUL_PAYMENT)

    dp.shipping_query.register(shipping_check)

    # dp.callback_query.register(select_macbook, MacInfo.filter())
    # with filter
    dp.callback_query.register(select_macbook, MacInfo.filter(F.model == "Pro"))
    dp.message.register(get_location, F.content_type == ContentType.LOCATION)
    dp.message.register(get_photo, F.content_type == ContentType.PHOTO)
    dp.message.register(get_hello, F.text == 'Привет')
    dp.message.register(get_true_contacts, F.content_type == ContentType.CONTACT, IsTrueContact())
    dp.message.register(get_fake_contacts, F.content_type == ContentType.CONTACT)
    dp.message.register(get_start, CommandStart)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
