from gc import callbacks

from aiogram import F, Router
from aiogram.types import CallbackQuery, Message
from Keyboard.inline import info_company
from configs.config import city, address

router = Router()


@router.callback_query(F.data=="info")
async def info(call:CallbackQuery):
    await call.answer()
    await call.message.edit_reply_markup("Вы выбрали информацию о нас, выберите что хотите знать",reply_markup=info_company())

@router.callback_query(F.data =="location")
async def location(call:CallbackQuery):
    await call.answer()
    await call.message.edit_reply_markup(callbacks.from_user.id ,"Наш Адресс:{city},{address}",reply_markup=info_company())
