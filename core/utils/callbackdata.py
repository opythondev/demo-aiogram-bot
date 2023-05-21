from aiogram.filters.callback_data import CallbackData


class MacInfo(CallbackData, prefix='mac'):
    """
    Attributes:
    model: str
    chip: str
    ram: str
    year: int
    """
    model: str
    chip: str
    ram: str
    year: int

