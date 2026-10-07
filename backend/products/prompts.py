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

def build_executor_prompt(product_name, features, plan, context):
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

External Product Context:
{context}

Requirements:
- Write 80–120 words.
- Mention the exact product name.
- Follow the Planner's main writing focus.
- Include every provided feature in the description.
- Use each provided feature explicitly, preferably using the original feature wording.
- Preserve feature names and specifications accurately.
- Highlight the important features naturally.
- Use professional and customer-friendly language.
- Do not invent features, specifications, benefits, performance claims, or product characteristics.
- Return only the product description.
- Use relevant information from the external context when appropriate.
- Incorporate relevant external information naturally into the description.
- Do not copy the external context directly.
- Do not treat external product specifications as specifications of the user's product.
- Do not invent claims based on price or rating.
- Do not mention price or rating unless the user asks for them.
- If external context conflicts with the user's provided features, always follow the user's provided features.
"""