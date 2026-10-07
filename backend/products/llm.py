from openai import OpenAI
from django.conf import settings
import json
from .tools import search_products

client = OpenAI(api_key=settings.OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1")

PRODUCT_SEARCH_TOOL = {
    "type": "function",
    "function": {
        "name": "search_products",
        "description": "Search the external product database for products related to the user's request.",
        "parameters": {
            "type": "object",
            "properties": {
                "search_term": {
                    "type": "string",
                    "description": "The product name or search term to look for."
                }
            },
            "required": ["search_term"]
        }
    }
}

def generate_product_description(prompt):
    products = []
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]

    response = client.chat.completions.create(
        model=settings.OPENROUTER_MODEL,
        messages=messages,
        tools=[PRODUCT_SEARCH_TOOL]
    )
    message = response.choices[0].message

    # Check whether the LLM requested a tool
    if message.tool_calls:
        messages.append(message)

        for tool_call in message.tool_calls:

            if tool_call.function.name == "search_products":

                arguments = json.loads(
                    tool_call.function.arguments
                )

                search_term = arguments["search_term"]

                # Python executes the actual function
                products = search_products(search_term)
                print("TOOL CALLED")
                print("SEARCH TERM:", search_term)
                print("PRODUCTS FOUND:", products)

                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": json.dumps(products)
                })

        # Send the tool result back to the LLM
        response = client.chat.completions.create(
            model=settings.OPENROUTER_MODEL,
            messages=messages,
            tools=[PRODUCT_SEARCH_TOOL]
        )

    return {
        "description": response.choices[0].message.content,
        "products": products
    }