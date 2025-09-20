from aiogram import F, Router
from aiogram.types import CallbackQuery, Message
from Keyboard.inline import info_company
from configs.config import city, adress

router = Router()


@router.callback_query(F.data=="info")
async def info(call:CallbackQuery):
    await call.answer()
    await call.message.edit_reply_markup("Вы выбрали информацию о нас, выберите что хотите знать",reply_markup=info_company())

@router.callback_query(F =="location")
async def location(message:Message):
    await message.answer()
 #   await call.message.edit_reply_markup(F"Наш адресc: {city}, {adress}")
