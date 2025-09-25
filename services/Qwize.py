from openai import AsyncOpenAI
from configs.config import OpenAI_KEY



client = AsyncOpenAI(api_key=OpenAI_KEY)

async def get_qwize(topic:str)->str:
    responses=await client.chat.completions.create(
        model="gpt-5-nano",
        messages=[
            {"role":"system", "content":f'Сгенирируй вопрос по теме {topic}'}]
    )
    return responses.choices[0].message.content



async def chek_answer(question:str,answer:str)->str:
    responses = await client.chat.completions.create(
        model="gpt-5-nano",
        messages=[
            {"role": "system", "content": f'Проверь правильность ответна на Qwize. Вопрос {question} Ответ {answer}. Скажи "правильно" или "не правильно"'}]
    )
    return responses.choices[0].message.content