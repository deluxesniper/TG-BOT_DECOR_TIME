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


def save_message(message_data):
    filename = "json/messages.json"

    try:
        # Всегда начинаем с пустого списка если есть ошибки
        messages = []

        # Пытаемся прочитать существующие данные
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read().strip()
                if content:  # Если файл не пустой
                    messages = json.loads(content)

        # Добавляем новое сообщение (структурированные данные)
        messages.append(message_data)

        # Сохраняем обратно
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(messages, f, ensure_ascii=False, indent=4)

    except Exception as e:
        print(f"Ошибка при сохранении: {e}")
        # Создаем файл с одним сообщением
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump([message_data], f, ensure_ascii=False, indent=4)


