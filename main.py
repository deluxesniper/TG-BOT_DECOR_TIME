import asyncio
from aiogram import Bot, Dispatcher, F
from configs.config import TOKEN
from handlers import router
import logging


async def main():
    logging.basicConfig(level=logging.INFO)
    dp = Dispatcher()
    bot = Bot(token=TOKEN)
    dp.include_router(router)
    await dp.start_polling(bot)



asyncio.run(main())