import json


def save_advertisement(user_id: int, username: str, text: str, filename: str = "save_advertisements.json"):
    # Данные для сохранения
    ad_data = {
        "user_id": user_id,
        "username": username,
        "text": text,
        "status": "active"
    }

