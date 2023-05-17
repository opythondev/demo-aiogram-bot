from aiogram import Bot
from aiogram.types import Message
import asyncio


async def get_start(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f"<b>Привет! {message.from_user.first_name}</b>")
    await message.answer(f"<s>Привет! {message.from_user.first_name}</s>")
    await message.reply(f"<tg-spoiler>Привет! {message.from_user.first_name}</tg-spoiler>")


async def get_photo(message: Message, bot: Bot):
    await message.answer(f"You send me a photo, I saved it")
    file = await bot.get_file(message.photo[-1].file_id)
    await bot.download_file(file.file_path, destination="photo.jpg")
