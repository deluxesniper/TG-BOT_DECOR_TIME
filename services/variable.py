from aiogram.fsm.context import FSMContext
from aiogram import types
import  json
import os
Adhesive = 7.5
Granella = 4
Kraft_pro_matt = 10
Durata = 10

async def Adhesive_calculate(message:types.Message, state:FSMContext, Adhesive:float):
    area = 35
    result = area / Adhesive
    print(result)
    await message.answer(f"С вашей площадью {area} м²\n Вам потребуется : {result:2f} Литров грунтовки \n рассход {Adhesive}м²/литр")
    await state.clear()
    return result

async def Granella_calculate(message:types.Message, state:FSMContext, Granella:float):
    area = 35
    result = area / Granella
    print(result)
    await message.answer(f"С вашей площадью {area} м²\n Вам потребуется <UNK>: {result:2f}Литров грунтовки \n рассход {Granella}м²/литр")
    await state.clear()
    return result


def save_message(my_messages):
    save_data_folder = "json/data.json"

    # Создаем папку если не существует
    os.makedirs(os.path.dirname(save_data_folder), exist_ok=True)

    try:
        # Пытаемся прочитать существующие данные
        with open(save_data_folder, mode='r', encoding='utf-8') as f:
            save_message = json.load(f)
    except FileNotFoundError:
        # Если файл не найден, начинаем с пустого списка
        save_message = []

    # Добавляем новое сообщение
    save_message.append(my_messages)

    # Записываем обратно
    with open(save_data_folder, mode='w', encoding='utf-8') as f:
        json.dump(save_message, f, ensure_ascii=False, indent=4)