from .llm import generate_product_description
from .prompts import build_planner_prompt

def create_product_plan(product_name, features):
    features_text = "\n".join(f"-{feature}" for feature in features) 
    prompt = build_planner_prompt(
        product_name,
        features
    )

    return generate_product_description(prompt)