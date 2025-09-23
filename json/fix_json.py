
import json
import os


def fix_json_file():
    """Исправляет поврежденный JSON файл"""
    ads_file = "data/advertisements.json"

    try:
        # Пытаемся прочитать файл
        with open(ads_file, 'r', encoding='utf-8') as f:
            content = f.read()
            print("Содержимое файла:")
            print(content)

        # Пробуем загрузить JSON
        with open(ads_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            print("Файл валиден!")

    except json.JSONDecodeError as e:
        print(f"Ошибка в файле: {e}")
        print("Создаю новый валидный файл...")

        # Создаем новый валидный файл
        with open(ads_file, 'w', encoding='utf-8') as f:
            json.dump([], f, ensure_ascii=False, indent=4)
        print("Файл исправлен!")

    except FileNotFoundError:
        print("Файл не найден, создаю новый...")
        os.makedirs('data', exist_ok=True)
        with open(ads_file, 'w', encoding='utf-8') as f:
            json.dump([], f, ensure_ascii=False, indent=4)
        print("Файл создан!")


if __name__ == "__main__":
    fix_json_file()