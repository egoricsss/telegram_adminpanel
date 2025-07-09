from typing import Any, Awaitable, Callable

from aiogram import BaseMiddleware
from aiogram.types import Message

from core import config

__all__ = ["AdminOnlyMiddleware"]


class AdminOnlyMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: dict[str, Any],
    ) -> Any:
        user_id = event.from_user.id
        if user_id == config.ADMIN_ID:
            return await handler(event, data)
        else:
            return None
