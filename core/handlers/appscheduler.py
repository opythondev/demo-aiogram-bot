from aiogram import Bot
from core.settings import settings


async def send_message_time(bot: Bot):
    await bot.send_message(settings.bots.admin_id, f"This message will be sent after few seconds on /start command")


async def send_message_cron(bot: Bot):
    await bot.send_message(settings.bots.admin_id, f"This message will be sent on every day at selected HH:MM")


async def send_message_interval(bot: Bot):
    await bot.send_message(settings.bots.admin_id, f"This message will be sent with 1 minute interval")