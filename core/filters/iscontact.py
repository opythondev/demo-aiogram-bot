from aiogram.filters import BaseFilter
from aiogram.types import Message


class IsTrueContact(BaseFilter):
    """
    Custom filter
    """
    async def __call__(self, message: Message):
        """

        :param message:
        :return:
        """
        if message.contact.user_id == message.from_user.id:
            return {'phone': message.contact.phone_number}
        return False
