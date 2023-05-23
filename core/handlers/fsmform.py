from datetime import datetime, timedelta
from aiogram import Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from core.utils.statesform import StepsForm
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from core.handlers.appscheduler import send_message_middleware


async def get_form(message: Message, state: FSMContext):
    await message.answer(f'{message.from_user.first_name}, начинаем заполнять анкету. Введите свое Имя')
    await state.set_state(StepsForm.GET_NAME)


async def get_name(message: Message, state: FSMContext):
    await message.answer(f'Ваше Имя: <b>{message.text}</b>\n\r\n\rВведите Фамилию')
    await state.update_data(name=message.text)
    await state.set_state(StepsForm.GET_LAST_NAME)


async def get_last_name(message: Message, state: FSMContext):
    await message.answer(f'Ваша Фамилия: <b>{message.text}</b>\n\r\n\rВведите Возраст')
    await state.update_data(last_name=message.text)
    await state.set_state(StepsForm.GET_AGE)


async def get_age(message: Message, bot: Bot, state: FSMContext, scheduler: AsyncIOScheduler):
    await message.answer(f'Ваш возраст: <b>{message.text}</b>\n\r\n\r')
    await state.update_data(age=message.text)
    context_data = await state.get_data()
    await message.answer(f'Данные в форме: {str(context_data)}\n\r\n\r')
    name = context_data.get('name')
    last_name = context_data.get('last_name')
    age = context_data.get('age')
    data_user = f"Ваши данные:\n\r" \
                f"Имя: {name}\n\r" \
                f"Фамилия: {last_name}\n\r" \
                f"Возраст: {age}"
    await message.answer(data_user)
    await state.clear()
    scheduler.add_job(send_message_middleware, trigger="date", run_date=datetime.now() + timedelta(seconds=10.0),
                      kwargs={'chat_id': message.from_user.id})
