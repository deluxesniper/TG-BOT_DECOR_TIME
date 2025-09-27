from openai import AsyncOpenAI
from configs.config import OpenAI_KEY
from aiogram.fsm.context import FSMContext


client = AsyncOpenAI(api_key=OpenAI_KEY)

async def get_quiz_question(topic:str)->str:
    responses=await client.chat.completions.create(
        model="gpt-5-nano",
        messages=[
            {"role":"system", "content":f'Сгенирируй вопрос по теме {topic}'}]
    )
    return responses.choices[0].message.content



async def check_answer(question: str, answer: str) -> str:
    response = await client.chat.completions.create(
        model="gpt-5-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    f"Проверь правильность ответа на квиз.\n"
                    f"Вопрос: {question}\n"
                    f"Ответ: {answer}\n"
                    'Скажи только одно слово: "правильно" или "неправильно".'
                ),
            }
        ],

    )
    print(response.choices[0].message.content.strip())
    return response.choices[0].message.content.strip()

async def get_score(state: FSMContext) -> int:
    data = await state.get_data()
    return data.get('score', 0)