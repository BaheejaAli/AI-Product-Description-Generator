from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductDescriptionSerializer
from .prompts import build_product_description_prompt
from .llm import generate_product_description
from .validator import validate_description

@api_view(["POST"])
def generate_description(request):
    serializer = ProductDescriptionSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    product_name = serializer.validated_data["product_name"]
    features = serializer.validated_data["features"]

    prompt = build_product_description_prompt(product_name, features)

    try:
        description = generate_product_description(prompt)

    except Exception:
        # to protect from API failure
        return Response({
                "error": "Unable to generate the product description right now. Please try again."
            },status=status.HTTP_502_BAD_GATEWAY)

    is_valid, result = validate_description(description)
    if not is_valid:
        return Response({
            "error":result
        },status=status.HTTP_502_BAD_GATEWAY)

    return Response({
        "description":result
    },status=status.HTTP_200_OK)


