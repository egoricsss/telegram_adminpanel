from aiogram.filters import Filter
from aiogram.types import Message
from config import config

__all__ = ["IsEgoric"]


class IsEgoric(Filter):
    async def __call__(self, message: Message) -> bool:
        return message.from_user.id == config.ADMIN_ID
