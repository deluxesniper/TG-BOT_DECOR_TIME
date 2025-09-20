from aiogram import F, Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(F.data == "info",)
async def info(call: CallbackQuery):
    await call.answer()
    await call.message.answer("Вы выбрали информацию о нас, выберите что хотите знать")
