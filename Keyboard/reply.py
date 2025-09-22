from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def menu():
    kb_list=[
        [KeyboardButton(text="Объявления")],
    ]

    keyboard = ReplyKeyboardMarkup(keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True)
    return keyboard


def under_the_menu():
    kb_list = [
        [KeyboardButton(text="Создать Объявление"),
         KeyboardButton(text="Мои Объявления")],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,  # автоматическое изменение размера
        one_time_keyboard=True  # скрыть после использования
    )
    return keyboard