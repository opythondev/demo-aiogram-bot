import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.types import ContentType
from aiogram.filters import CommandStart, Command

from core.handlers.basic import get_start, get_photo, get_hello, get_location, get_inline
from core.handlers.contact import get_fake_contacts, get_true_contacts
from core.handlers.callback import select_macbook
from core.filters.iscontact import IsTrueContact
from core.settings import settings
from core.utils.commands import set_commands

from core.utils.callbackdata import MacInfo


async def on_start(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, text="Bot был запущен")


async def on_stop(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text="Bot был остановлен")


async def start():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(name)s -"
                               " (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
                        )

    bot = Bot(settings.bots.bot_token, parse_mode='HTML')
    dp = Dispatcher()

    dp.startup.register(on_start)
    dp.shutdown.register(on_stop)

    # Хэндлеры отрабатывают по порядку, сверху вниз
    dp.message.register(get_inline, Command(commands=["inline"]))
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
