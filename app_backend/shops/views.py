from rest_framework import viewsets
from rest_framework import permissions
from app_backend.shops.models import Shop
from app_backend.shops.serializers import ShopSerializer


class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all().order_by('name')
    serializer_class = ShopSerializer
    permission_classes = [permissions.AllowAny]
