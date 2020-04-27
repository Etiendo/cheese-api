from django.contrib.auth.models import User
from app_backend.models import Shop
from rest_framework import viewsets
from rest_framework import permissions
from serializers import UserSerializer, ShopSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all().order_by('name')
    serializer_class = ShopSerializer
    permission_classes = [permissions.IsAuthenticated]
