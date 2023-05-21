from aiogram.types import CallbackQuery
from core.utils.callbackdata import MacInfo


# async def select_macbook(call: CallbackQuery):
#     model = call.data.split('_')[1]
#     chip = call.data.split('_')[2]
#     ram = call.data.split('_')[4]
#     year = call.data.split('_')[3]
#     answer = f'{call.message.from_user.first_name}, вы выбрали Macbook' \
#              f' модель {model}, chip {chip}, ram {ram}, year {year}'
#     await call.message.answer(answer)
#     await call.answer()

async def select_macbook(call: CallbackQuery, callback_data: MacInfo):
    model = callback_data.model
    chip = callback_data.chip
    ram = callback_data.ram
    year = callback_data.year
    answer = f'{call.message.from_user.first_name}, вы выбрали Macbook' \
             f' модель {model}, chip {chip}, ram {ram}, year {year}'
    await call.message.answer(answer)
    await call.answer()
