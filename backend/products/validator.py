def validate_description(description):
    # to protect from bad AI response
    if not description:
        return False, "AI returned an empty description."

    if not isinstance(description, str):
        return False, "AI returned an invalid response."

    description = description.strip()

    if len(description) < 20:
        return False, "AI description is too short."

    return True, description