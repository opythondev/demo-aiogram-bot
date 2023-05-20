from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder

reply_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Row 1, Btn 1'
        ),
        KeyboardButton(
            text='Row 1, Btn 2'
        ),
        KeyboardButton(
            text='Row 1, Btn 3'
        )
    ],
    [
        KeyboardButton(
            text='Row 2, Btn 1'
        ),
        KeyboardButton(
            text='Row 2, Btn 2'
        ),
        KeyboardButton(
            text='Row 2, Btn 3'
        ),
        KeyboardButton(
            text='Row 2, Btn 4'
        )
    ],
    [
        KeyboardButton(
            text='Row 3, Btn 1'
        ),
        KeyboardButton(
            text='Row 3, Btn 2'
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Choose the button', selective=True)


loc_tel_poll_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Send geolocation',
            request_location=True
        )
    ],
    [
        KeyboardButton(
            text='Send contact',
            request_contact=True
        )
    ],
    [
        KeyboardButton(
            text='Create poll',
            request_poll=KeyboardButtonPollType()
        )
    ]
], resize_keyboard=True, one_time_keyboard=False, input_field_placeholder='Send contact, location or create poll')


def get_reply_keyboard():
    keyboard_builder = ReplyKeyboardBuilder()
    keyboard_builder.button(text='Button 1')
    keyboard_builder.button(text='Button 2')
    keyboard_builder.button(text='Button 3')
    keyboard_builder.button(text='Send location', request_location=True)
    keyboard_builder.button(text='Send contact', request_contact=True)
    keyboard_builder.button(text='Create poll', request_poll=KeyboardButtonPollType())
    # set number of buttons in row
    keyboard_builder.adjust(3, 2, 1)
    return keyboard_builder.as_markup(resize_keyboard=True, one_time_keyboard=False,
                                      input_field_placeholder='Send contact, location or create poll')


