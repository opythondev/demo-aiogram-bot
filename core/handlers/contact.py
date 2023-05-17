from aiogram.types import Message
from aiogram import Bot


async def get_true_contacts(message: Message, bot: Bot, phone: str):
    await message.answer(f"ты отправил <b>свой</b> контакт {phone}")


async def get_fake_contacts(message: Message, bot: Bot):
    await message.answer(f"ты отправил <b>чужой</b> контакт")

