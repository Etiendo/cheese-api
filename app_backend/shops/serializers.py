from rest_framework import serializers
from app_backend.shops.models import Shop


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'
