def build_product_description_prompt(product_name, features):
    features_text = "\n".join(
        f"- {feature}" for feature in features
    )

    return f"""
You are a professional product copywriter.

Generate a clear and engaging product description based only
on the product information provided.

Product Name:
{product_name}

Features:
{features_text}

Requirements:
- Write 80–120 words.
- Highlight the important features naturally.
- Use professional and customer-friendly language.
- Do not invent features or specifications.
- Return only the product description.
"""