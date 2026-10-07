from .llm import generate_product_description
from .prompts import build_executor_prompt


def generate_product_description_with_plan(
    product_name,
    features,
    plan,
    context
):
    prompt = build_executor_prompt(
        product_name,
        features,
        plan,
        context
    )

    return generate_product_description(prompt)