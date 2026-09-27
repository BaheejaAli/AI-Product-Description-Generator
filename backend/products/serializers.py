from rest_framework import serializers

class ProductDescriptionSerializer(serializers.Serializer):
    product_name = serializers.CharField(required=True, allow_blank=False)
    features = serializers.ListField(required=True, allow_empty=False,
                child=serializers.CharField(allow_blank=False))