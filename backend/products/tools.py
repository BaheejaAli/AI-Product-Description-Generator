import requests


def search_products(search_term):
    """
    Search the external product database for relevant products.
    """

    url = "https://dummyjson.com/products/search"

    response = requests.get(
        url,
        params={"q": search_term},
        timeout=10
    )

    response.raise_for_status()
    data = response.json()
    products = data.get("products", [])
    if products:
        return products[:3]

    words = search_term.lower().split()
    relevant_words = [
        word for word in words
        if len(word) >= 4
    ]

    found_products = []

    for word in relevant_words:
        response = requests.get(
            url,
            params={"q": word},
            timeout=10
        )

        response.raise_for_status()
        data = response.json()

        for product in data.get("products", []):
            if product not in found_products:
                found_products.append(product)

            if len(found_products) >= 3:
                return found_products

    return found_products
