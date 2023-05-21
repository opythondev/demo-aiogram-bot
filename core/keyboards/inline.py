from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


select_macbook = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Mac Book Air m1 2020 8Gb",
            callback_data="macbook_Air_m1_2020_8Gb"
        ),
        InlineKeyboardButton(
            text="Mac Book Air m2 2022 16Gb",
            callback_data="macbook_Air_m2_2022_16Gb"
        )
    ],
    [
        InlineKeyboardButton(
            text="Mac Book Pro m1 2020 16Gb",
            callback_data="macbook_Pro_m1_2020_16Gb"
        ),
        InlineKeyboardButton(
            text="Mac Book Pro m2 2023 16Gb",
            callback_data="macbook_Pro_m2_2023_16Gb"
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


def get_inline_keyboard():
    keyboard_builder = InlineKeyboardBuilder()

    keyboard_builder.button(text="Mac Book Air m1 2020 8Gb", callback_data="macbook_Air_m1_2020_8Gb")
    keyboard_builder.button(text="Mac Book Air m2 2022 16Gb", callback_data="macbook_Air_m2_2022_16Gb")
    keyboard_builder.button(text="Mac Book Pro m1 2020 16Gb", callback_data="macbook_Pro_m1_2020_16Gb")
    keyboard_builder.button(text="Mac Book Pro m2 2023 16Gb", callback_data="macbook_Pro_m2_2023_16Gb")
    keyboard_builder.button(text="Open Site", url="https://google.com")
    keyboard_builder.button(text="Profile", url="tg://user?id=6213341124")

    keyboard_builder.adjust(2, 2, 1, 1)
    return keyboard_builder.as_markup()

