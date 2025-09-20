from aiogram import Router
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.filters import Command

router = Router()

@router.message(Command('start'))
async def start(message: Message):
    await message.answer(f"""Здравствуйте! {message.from_user.full_name} \nВас приветствует компания ООО «ДекорТайм»\nОфициальный дистрибьютор производителей декоративных покрытий:
Cebos Color, Valpaint, San Marco, Ticiana Deluxe, Werth Deco и представитель лакокрасочной продукции Flugger.\n\nМожете ознакомиться с моими функциями ниже""", reply_markup=info_inline())


@router.callback_query(F.data=="info")
async def info(call:CallbackQuery):
    await call.answer()
    await call.message.answer("Вы выбрали информацию о нас, выберите что хотите знать")
