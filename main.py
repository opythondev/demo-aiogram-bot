import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ContentType
from aiogram.filters import Command, CommandStart

from core.handlers.basic import get_start, get_photo, get_hello
from core.settings import settings


async def on_start(bot: Bot):
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
    dp.message.register(get_photo, F.content_type == ContentType.PHOTO)
    dp.message.register(get_hello, F.text == 'Привет')
    dp.message.register(get_start, CommandStart)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
