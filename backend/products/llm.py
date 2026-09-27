from openai import OpenAI
from django.conf import settings

client = OpenAI(api_key=settings.OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1")

def generate_product_description(prompt):
    response = client.chat.completions.create(
        model=settings.OPENROUTER_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response.choices[0].message.content