from aiogram import Bot
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery


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
        photo_url="http://klublady.ru/uploads/posts/2022-02/1644751985_51-klublady-ru-p-shokoladnie-kapkeiki-s-shokoladnim-kremom-53.jpg",
        photo_size=100,
        photo_width=800,
        photo_height=450,
        need_name=True,
        need_phone_number=True,
        need_email=True,
        need_shipping_address=False,
        send_phone_number_to_provider=False,
        send_email_to_provider=False,
        is_flexible=False,
        disable_notification=False,
        protect_content=False,
        reply_to_message_id=None,
        allow_sending_without_reply=True,
        reply_markup=None,
        request_timeout=15
    )


async def pre_checkout_query(pre_checkout: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout.id, ok=True)


async def successful_payment(message: Message):
    message_answer = f"Спасибо за оплату {message.successful_payment.total_amount / 100} {message.successful_payment.currency}" \
              f"Ссылка на скачивание курса https://google.com"
    await message.answer(message_answer)
