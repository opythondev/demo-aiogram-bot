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
            command='form',
            description='New Form Input'
        ),
        BotCommand(
            command='inline',
            description='Show Inline KB'
        ),
        BotCommand(
            command='pay',
            description='Test payments'
        )
    ]

    await bot.set_my_commands(commands, scope=BotCommandScopeDefault())
