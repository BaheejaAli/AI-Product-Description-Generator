from .llm import generate_product_description
from .prompts import build_executor_prompt


def generate_product_description_with_plan(
    product_name,
    features,
    plan
):
    prompt = build_executor_prompt(
        product_name,
        features,
        plan
    )

    return generate_product_description(prompt)