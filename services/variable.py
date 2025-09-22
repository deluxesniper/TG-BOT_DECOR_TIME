from aiogram.fsm.context import FSMContext
from aiogram import types

Adhesive = 7.5
Granella = 4
Kraft_pro_matt = 10
Durata = 10

async def Adhesive_calculate(message:types.Message, state:FSMContext, Adhesive:float):
    area = 35
    result = area / Adhesive
    print(result)
    await message.answer(f"С вашей площадью {area} м²\n Вам потребуется <UNK>: {result:2f}Литров грунтовки \n рассход {Adhesive}м²/литр")
    await state.clear()
    return result

async def Granella_calculate(message:types.Message, state:FSMContext, Granella:float):
    area = 35
    result = area / Granella
    print(result)
    await message.answer(f"С вашей площадью {area} м²\n Вам потребуется <UNK>: {result:2f}Литров грунтовки \n рассход {Granella}м²/литр")
    await state.clear()
    return result
