import os
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types.input_file import FSInputFile
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web

from command_handlers import (
    add_router,
    base_router,
    clientlist_router,
    remove_router,
    qr_router,
)
from core import config

sys.path.insert(1, os.path.join(sys.path[0], ".."))


async def on_startup(bot: Bot) -> None:
    await bot.set_webhook(
        url=f"{config.BASE_WEBHOOK_URL}{config.WEBHOOK_PATH}",
        secret_token=config.WEBHOOK_SECRET,
        certificate=FSInputFile(config.CERTIFICATE_PATH),
    )


def main() -> None:
    dp = Dispatcher()
    dp.include_routers(
        clientlist_router, add_router, remove_router, qr_router, base_router
    )
    dp.startup.register(on_startup)
    bot = Bot(
        token=config.TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    app = web.Application()
    webhook_request_handler = SimpleRequestHandler(
        dispatcher=dp, bot=bot, secret_token=config.WEBHOOK_SECRET
    )
    webhook_request_handler.register(app, path=config.WEBHOOK_PATH)
    setup_application(app, dp, bot=bot)
    web.run_app(app, host=config.WEB_SERVER_HOST, port=config.WEB_SERVER_PORT)


if __name__ == "__main__":
    main()
