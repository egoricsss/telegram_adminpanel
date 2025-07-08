from aiogram import Bot, Dispatcher
from config import config
from bot import router
from aiohttp import web
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiogram.types.input_file import FSInputFile


async def on_startup(bot: Bot) -> None:
    await bot.set_webhook(
        url=f"{config.BASE_WEBHOOK_URL}{config.WEBHOOK_PATH}",
        secret_token=config.WEBHOOK_SECRET,
        certificate=FSInputFile(config.CERTIFICATE_PATH)
    )


def main() -> None:
    dp = Dispatcher()
    dp.include_router(router)
    dp.startup.register(on_startup)
    bot = Bot(token=config.TOKEN)
    app = web.Application()
    webhook_request_handler = SimpleRequestHandler(
        dispatcher=dp, bot=bot, secret_token=config.WEBHOOK_SECRET
    )
    webhook_request_handler.register(app, path=config.WEBHOOK_PATH)
    setup_application(app, dp, bot=bot)
    web.run_app(app, host=config.WEB_SERVER_HOST, port=config.WEB_SERVER_PORT)


if __name__ == "__main__":
    main()
