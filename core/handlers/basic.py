"""Basic handlers"""
import json

from aiogram import Bot
from aiogram.types import Message
from core.keyboards.reply import reply_keyboard, loc_tel_poll_keyboard, get_reply_keyboard
from core.keyboards.inline import select_macbook, get_inline_keyboard


async def get_inline(message: Message):
    await message.answer(f"Привет! {message.from_user.first_name}.\nОтображаю инлайн клавиатуру",
                         reply_markup=get_inline_keyboard())


async def get_start(message: Message, counter: str):
    await message.answer(f"Message /start count: {counter}")
    await message.answer(f"<s>Привет! {message.from_user.first_name}</s>", reply_markup=get_reply_keyboard())


async def get_location(message: Message):
    await message.answer(f"You send location\n\r"
                         f"latitude: {message.location.latitude}\nlongtitude: {message.location.longitude}")


async def get_photo(message: Message, bot: Bot):
    await message.answer(f"You send me a photo, I saved it")
    file = await bot.get_file(message.photo[-1].file_id)
    await bot.download_file(file.file_path, destination="photo.jpg")


async def get_hello(message: Message):
    await message.answer(f"И тебе привет!")
    json_str = json.dumps(message.dict(), default=str)
    print(json_str)
