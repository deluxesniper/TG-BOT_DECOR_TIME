from aiogram.fsm.context import FSMContext
from aiogram import types

Adhesive = 7.5
Granella = 4
Kraft_pro_matt = 10
Durata = 10

async def Adhesive_calculate(message:types.Message, state:FSMContext, Adhesive:float):
    area = float(message.text)
    result = area / Adhesive
    await message.answer(f"С вашей площадью {area} м²\n Вам потребуется <UNK>: {result:2f}Литров грунтовки \n рассход {Adhesive}м²/литр")
    await state.clear()
    return result