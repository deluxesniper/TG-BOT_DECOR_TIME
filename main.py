import asyncio
from aiogram import Bot, Dispatcher, F
from logs.logs import logging
from configs.config import TOKEN
from handlers import Router, router


async def main():
    logging.basicConfig(level=logging.INFO)
    dp = Dispatcher()
    bot = Bot(token=TOKEN)
    dp.include_router(router)
    await dp.start_polling(bot)



asyncio.run(main())