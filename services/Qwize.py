from http.client import responses

from openai import OpenAI

from services.gpt_random_fact import client


async def get_qwize():
    responses=client.chat.completions.create(
        model="gpt-5-nano",
        messages=[
            {"role":"system", "content":"Давай с тобой поиграем в игру Квиз"},
            {'role': 'user', 'content': 'Факт как появились краски на земле и где они сначала использовались'}
    )