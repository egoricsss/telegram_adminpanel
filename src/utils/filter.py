from aiogram.filters import Filter
from aiogram.types import Message

from core import config

__all__ = ["IsAdmin"]


class IsAdmin(Filter):
    async def __call__(self, message: Message) -> bool:
        return message.from_user.id == config.ADMIN_ID
