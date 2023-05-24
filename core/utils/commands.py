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
        ),
        BotCommand(
            command='audio',
            description='Send audio'
        ),
        BotCommand(
            command='document',
            description='Send document'
        ),
        BotCommand(
            command='mediagroup',
            description='Send mediagroup'
        ),
        BotCommand(
            command='photo',
            description='Send photo'
        ),
        BotCommand(
            command='sticker',
            description='Send sticker'
        ),
        BotCommand(
            command='video',
            description='Send video'
        ),
        BotCommand(
            command='video_note',
            description='Send video note'
        ),
        BotCommand(
            command='voice',
            description='Send voice'
        )
    ]

    await bot.set_my_commands(commands, scope=BotCommandScopeDefault())
