def validate_description(
    description,
    product_name=None,
):
    if not description:
        return False, "AI returned an empty description."

    if not isinstance(description, str):
        return False, "AI returned an invalid response."

    if product_name and product_name.lower() not in description.lower():
        return False, "AI description does not mention the product name."

    return True, description.strip()
