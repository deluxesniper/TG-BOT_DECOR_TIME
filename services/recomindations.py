from http.client import responses
from platform import system

from openai import AsyncOpenAI
from configs.config import OpenAI_KEY
from aiogram.fsm.context import FSMContext


client = AsyncOpenAI(api_key=OpenAI_KEY)


async def recommendations_move(films:str)->str:
    responses=await client.chat.completions.create(
        model="gpt-5-mini",
        messages=[
            {"role":"system","content":f" Подскажи мне по 5 фильмов  каждого года,  из жанра{films}  за 2022 по 2024 год  "}
        ]
    )
    return  responses.choices[0].message.content
