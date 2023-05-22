from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
import asyncpg
from aiogram.types import TelegramObject
from core.utils.dbconnect import Request


class DbSession(BaseMiddleware):
    def __init__(self, connection: asyncpg.pool.Pool):
        super().__init__()
        self.connection = connection

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:
        async with self.connection.acquire() as connect:
            data['request'] = Request(connect)
            return await handler(event, data)

