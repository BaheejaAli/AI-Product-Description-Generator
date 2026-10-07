from .planner import create_product_plan
from .executor import generate_product_description_with_plan
from .validator import validate_description


def run_product_workflow(product_name, features):
    # Step 1: Planner
    plan = create_product_plan(
        product_name,
        features
    )

    # Step 2: Executor
    llm_result = generate_product_description_with_plan(
        product_name,
        features,
        plan
    )

    description = llm_result["description"]
    products = llm_result["products"]

    # Step 3: Validator
    is_valid, result = validate_description(
        description, product_name
    )

    # Step 4: Retry if validation fails
    if not is_valid:
        llm_result = generate_product_description_with_plan(
            product_name,
            features,
            plan
        )

        description = llm_result["description"]
        products = llm_result["products"]

        is_valid, result = validate_description(
            description, product_name
        )


    return {
        "plan": plan,
        "description": result,
        "products": products,
        "is_valid": is_valid,
    }

