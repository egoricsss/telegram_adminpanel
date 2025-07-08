from aiogram.filters import Filter
from aiogram.types import Message
from config import config

__all__ = ["IsEgoric"]


class IsEgoric(Filter):
    def __call__(message: Message) -> bool:
        return message.from_user.id == config.ADMIN_ID
