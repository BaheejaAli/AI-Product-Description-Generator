from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import ProductDescriptionSerializer
from .workflow import run_product_workflow


@api_view(["POST"])
def generate_description(request):
    serializer = ProductDescriptionSerializer(data=request.data)

    if not serializer.is_valid():
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    product_name = serializer.validated_data["product_name"]
    features = serializer.validated_data["features"]

    try:
        result = run_product_workflow(
            product_name,
            features
        )

    except Exception:
        return Response(
            {
                "error": (
                    "Unable to generate the product description "
                    "right now. Please try again."
                )
            },
            status=status.HTTP_502_BAD_GATEWAY
        )

    if not result["is_valid"]:
        return Response(
            {
                "error": result["description"]
            },
            status=status.HTTP_502_BAD_GATEWAY
        )

    return Response(
        {
            "description": result["description"]
        },
        status=status.HTTP_200_OK
    )