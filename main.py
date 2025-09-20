import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from logs.logs import logging
from configs.config import TOKEN
from Keyboard.inline import info_inline

dp=Dispatcher()
bot=Bot(token=TOKEN)


async def main():
    await dp.start_polling(bot)


@dp.message(Command('start'))
async def start(message: Message):
    await message.answer(f"""Здравствуйте! {message.from_user.full_name} \nВас приветствует компания ООО «ДекорТайм»\nОфициальный дистрибьютор производителей декоративных покрытий:
Cebos Color, Valpaint, San Marco, Ticiana Deluxe, Werth Deco и представитель лакокрасочной продукции Flugger.\n\nМожете ознакомиться с моими функциями ниже""", reply_markup=info_inline())




asyncio.run(main())