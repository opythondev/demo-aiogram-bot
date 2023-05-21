from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

select_macbook = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Mac Book Air m1 2020 8Gb",
            callback_data="Air_m1_2020_8Gb"
        ),
        InlineKeyboardButton(
            text="Mac Book Air m2 2022 16Gb",
            callback_data="Air_m2_2022_16Gb"
        )
    ],
    [
        InlineKeyboardButton(
            text="Mac Book Pro m1 2020 16Gb",
            callback_data="Pro_m1_2020_16Gb"
        ),
        InlineKeyboardButton(
            text="Mac Book Pro m2 2023 16Gb",
            callback_data="Pro_m2_2023_16Gb"
        )
    ],
    [
        InlineKeyboardButton(
            text="Open Site",
            url="https://google.com"
        ),
        InlineKeyboardButton(
            text="Profile",
            url="tg://user?id=6213341124"
        )
    ]
])
