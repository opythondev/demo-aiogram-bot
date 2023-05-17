from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='Start command descr'
        ),
        BotCommand(
            command='help',
            description='Help command descr'
        ),
        BotCommand(
            command='cancel',
            description='Cancel command descr'
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault)
