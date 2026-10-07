from .planner import create_product_plan
from .executor import generate_product_description_with_plan
from .validator import validate_description

import requests


def run_product_workflow(product_name, features):
    # Step 1: Planner
    plan = create_product_plan(
        product_name,
        features
    )

    # Step 2: Retrieve external product data
    products = retrieve_products(product_name)

    # Step 3: Build context
    context = build_product_context(products)

    # Step 4: Executor
    description = generate_product_description_with_plan(
        product_name,
        features,
        plan, 
        context
    )

    # Step 5: Validator
    is_valid, result = validate_description(
        description, product_name
    )

    # Step 6: Retry if validation fails
    if not is_valid:
        description = generate_product_description_with_plan(
            product_name,
            features,
            plan,
            context
        )

        is_valid, result = validate_description(
            description, product_name
        )


    return {
        "plan": plan,
        "context" : context,
        "description": result,
        "is_valid": is_valid,
    }



def get_products_from_api(search_term):
    url = "https://dummyjson.com/products/search"

    response = requests.get(
        url,
        params={"q": search_term},
        timeout=10
    )

    response.raise_for_status()

    return response.json()

# ============================================================
# RETRIEVAL PROCESS
# ============================================================

def retrieve_products(product_name):
    data = get_products_from_api(product_name)

    products = data["products"]

    relevant_products = []

    for product in products:
        text = (
            product["title"]
            + " "
            + product["category"]
            + " "
            + product["description"]
            + " "
            + " ".join(product["tags"])
        ).lower()

        if product_name.lower() in text:
            relevant_products.append(product)

    return relevant_products[:3]

# ============================================================
# CONTEXT BUILDING
# ============================================================

def build_product_context(products):
    context = "\n".join(
        f"""
Brand: {product['brand']}
Category: {product['category']}
Product: {product['title']}
Description: {product['description']}
Price: ${product['price']}
Rating: {product['rating']}
Tags: {', '.join(product['tags'])}
"""
        for product in products
    )

    return context