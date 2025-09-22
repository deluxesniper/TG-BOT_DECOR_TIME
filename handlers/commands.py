from aiogram import Router ,F
from aiogram.types import Message
from Keyboard.inline import info_inline
from Keyboard.reply import  menu
from aiogram.filters import Command
from aiogram.types import CallbackQuery
from services.gpt_random_fact import get_fact

router = Router()

@router.message(Command('start'))
async def start(message: Message):
    await message.answer(f"""Здравствуйте! {message.from_user.full_name} \nВас приветствует компания ООО «ДекорТайм»\nОфициальный дистрибьютор производителей декоративных покрытий:
Cebos Color, Valpaint, San Marco, Ticiana Deluxe, Werth Deco и представитель лакокрасочной продукции Flugger.\n\nМожете ознакомиться с моими функциями ниже""", reply_markup=info_inline(), )



@router.message(Command('add'))
async def add(message: Message):
    await message.answer(f"Здравствуйте! {message.from_user.full_name} хотите создать обьявление?", reply_markup=menu())















