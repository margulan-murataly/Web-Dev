from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'discount', 'rating', 'images']

    def get_discount(self, obj):
        if obj.price:
            return round(float(obj.price) * 0.9, 2)
        return 0
