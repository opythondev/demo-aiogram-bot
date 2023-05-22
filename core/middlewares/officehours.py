from datetime import datetime
from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import Message, TelegramObject


def office_hours() -> bool:
    return datetime.now().weekday() in (0, 1, 2, 3, 4) and datetime.now().hour in ([i for i in range(8, 19)])


class OfficeHoursMiddleware(BaseMiddleware):

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        """

        :param handler: Use Message OR TelegramObject to handle any updates
        :param event: Use Message OR TelegramObject to handle any updates
        :param data:
        :return:
        """
        if not office_hours():
            return await handler(event, data)
        # IF event type == Message
        # await event.answer("We are open from Monday to Friday\n\rWorking hours: 8-19\n\rText us later🤖")
