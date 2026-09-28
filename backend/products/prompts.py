def build_planner_prompt(product_name, features):
    features_text = "\n".join(
        f"- {feature}" for feature in features
    )

    return f"""
You are a product planning assistant.

Analyze the following product information and create a simple
plan for writing its product description.

Product Name:
{product_name}

Features:
{features_text}

Include:
- Product type
- All provided features
- Most important features
- Main writing focus

Important:
- Include all provided features in the plan.
- Do not omit any feature.
- Do not invent features or specifications.
- Preserve feature names and specifications accurately.

Return only the planning information.
"""

def build_executor_prompt(product_name, features, plan):
    features_text = "\n".join(
        f"- {feature}" for feature in features
    )

    return f"""
You are a professional product copywriter.

Create a product description using the original product
information and the plan created by the Planner.

Product Name:
{product_name}

Features:
{features_text}

Planner's Plan:
{plan}

Requirements:
- Write 80–120 words.
- Mention the exact product name.
- Follow the Planner's main writing focus.
- Include every provided feature in the description.
- Use each provided feature explicitly, preferably using the original feature wording.
- Preserve feature names and specifications accurately.
- Highlight the important features naturally.
- Use professional and customer-friendly language.
- Do not invent features or specifications.
- Return only the product description.
"""