from gc import callbacks

from aiogram import F, Router
from aiogram.types import CallbackQuery, Message
from Keyboard.inline import info_company, info_stor
from services.gpt_random_fact import get_fact
from stor.contacts import XL_city, XL_email, XL_phone,XL_opening_hours,XL_address



router = Router()


@router.callback_query(F.data=="info")
async def info(call:CallbackQuery):
    await call.answer()
    await call.message.edit_reply_markup("Вы выбрали информацию о нас, выберите что хотите знать",reply_markup=info_company())



@router.callback_query(F.data =="Locations")
async def location(call:CallbackQuery):
    await  call.answer()
    await call.message.answer(f"Наш адрес: {XL_city} {XL_address}\n время работы: {XL_opening_hours}\n телефон: {XL_phone}\n EMAIL@: {XL_email}")



@router.callback_query(F.data =="stors")
async def stors(call:CallbackQuery):
    await call.answer()
    await call.message.answer("Адреса наших магазинов",reply_markup=info_stor())



@router.callback_query(F.data =="random_fact")
async def random_nandler(call:CallbackQuery):
    await call.answer('Щас раскажу как появились краски, каждая история рандомна',show_alert=True)
    fact = await get_fact()
    await call.message.answer(f'Факт: {fact}')
