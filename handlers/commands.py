from aiogram import Router ,F
from aiogram.types import Message
from Keyboard.inline import info_inline, info_company
from aiogram.filters import Command
from aiogram.types import CallbackQuery
from configs.config import city, adress

router = Router()

@router.message(Command('start'))
async def start(message: Message):
    await message.answer(f"""Здравствуйте! {message.from_user.full_name} \nВас приветствует компания ООО «ДекорТайм»\nОфициальный дистрибьютор производителей декоративных покрытий:
Cebos Color, Valpaint, San Marco, Ticiana Deluxe, Werth Deco и представитель лакокрасочной продукции Flugger.\n\nМожете ознакомиться с моими функциями ниже""", reply_markup=info_inline())



@router.callback_query(F =="locations")
async def location(call: CallbackQuery):
    await call.answer()
    await call.message.edit_text(f'Наш адресс: {city}, {adress}')





