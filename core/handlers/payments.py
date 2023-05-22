from aiogram import Bot
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery, InlineKeyboardMarkup, InlineKeyboardButton, \
    ShippingOption, ShippingQuery


keyboards = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Оплата", pay=True),
        InlineKeyboardButton(text="URL", url="https://google.com")
    ]
])


BY_SHIPPING = ShippingOption(
    id="by",
    title="Shipping to Belarus",
    prices=[
        LabeledPrice(label="BY Shipping", amount=10000)
    ]
)

RU_SHIPPING = ShippingOption(
    id="ru",
    title="Shipping to Russia",
    prices=[
        LabeledPrice(label="RU EMS Shipping", amount=20000)
    ]
)

KZ_SHIPPING = ShippingOption(
    id="kz",
    title="Shipping to Khazakstan",
    prices=[
        LabeledPrice(label="KZ DHL Shipping", amount=30000)
    ]
)

CITIES_SHIPPING = ShippingOption(
    id="capitals",
    title="Доставка по городу",
    prices=[
        LabeledPrice(label="Курьер Иван", amount=2000)
    ]
)


async def shipping_check(query: ShippingQuery, bot: Bot):
    shipping_options = []
    countries = ["RU", "BY", "KZ"]
    cities = ["Москва", "Минск", "Астана"]

    if query.shipping_address.country_code not in countries:
        return await bot.answer_shipping_query(query.id, ok=False,
                                               error_message="Shipping to selected country not provided")
    if query.shipping_address.country_code == "BY":
        shipping_options.append(BY_SHIPPING)
    elif query.shipping_address.country_code == "RU":
        shipping_options.append(RU_SHIPPING)
    elif query.shipping_address.country_code == "KZ":
        shipping_options.append(KZ_SHIPPING)

    if query.shipping_address.city in cities:
        shipping_options.append(CITIES_SHIPPING)

    await bot.answer_shipping_query(query.id, ok=True, shipping_options=shipping_options)


async def order(message: Message, bot: Bot):
    await bot.send_invoice(
        chat_id=message.from_user.id,
        title="Покупка через бота",
        description="Bot order description",
        payload="Payment throught bot",
        provider_token="381764678:TEST:57492",
        currency="rub",
        prices=[
            LabeledPrice(
                label="Product Price",
                amount=99000
            ),
            LabeledPrice(
                label="NDS",
                amount=20000
            ),
            LabeledPrice(
                label="Discount",
                amount=-20000
            ),
            LabeledPrice(
                label="Bonus",
                amount=-40000
            )
        ],
        max_tip_amount=5000,
        suggested_tip_amounts=[1000, 2000, 3000, 4000],
        start_parameter='bot',
        provider_data=None,
        photo_url=None,
        photo_size=100,
        photo_width=400,
        photo_height=350,
        need_name=False,
        need_phone_number=False,
        need_email=False,
        need_shipping_address=False,
        send_phone_number_to_provider=False,
        send_email_to_provider=False,
        is_flexible=True,
        disable_notification=False,
        protect_content=False,
        reply_to_message_id=None,
        allow_sending_without_reply=True,
        reply_markup=keyboards,
        request_timeout=15
    )


async def pre_checkout_query(pre_checkout: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout.id, ok=True)


async def successful_payment(message: Message):
    message_answer = f"Спасибо за оплату {message.successful_payment.total_amount / 100} {message.successful_payment.currency}" \
              f"Ссылка на скачивание курса https://google.com"
    await message.answer(message_answer)
