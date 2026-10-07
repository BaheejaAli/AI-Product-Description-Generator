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
You are a professional product copywriter and product research assistant.

Your task is to create a product description based on the user's
product information and the Planner's plan.

Product Name:
{product_name}

Features:
{features_text}

Planner's Plan:
{plan}

You have access to a tool called 'search_products'.

Use the 'search_products' tool to retrieve relevant external
product information before generating the final description.

Use the retrieved information only as supporting context.
Do not treat retrieved products as the user's exact product.
Do not copy another product's specifications into the user's product.

Requirements:
- Write 80–120 words.
- Mention the exact product name.
- Follow the Planner's main writing focus.
- Include every provided feature.
- Preserve feature names and specifications accurately.
- Do not invent features or specifications.
- Use external product information only when relevant.
- Do not mention price or rating in the description unless requested.
- Return only the product description.
"""