from rest_framework import serializers
from .models import Shop, Category, Product


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Shop


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Category


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Product

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
