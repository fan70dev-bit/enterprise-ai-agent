from openai import OpenAI

from app.core.config import settings


client = OpenAI(
    api_key=settings.DEEPSEEK_API_KEY,
    base_url="https://api.deepseek.com",
)



def chat(
    messages:list,
):

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages,
        temperature=0.3,
    )


    return response.choices[0].message.content