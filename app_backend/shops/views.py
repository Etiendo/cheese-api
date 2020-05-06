import django_filters
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics
from django_filters import rest_framework as filters
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from app_backend.shops.models import Shop
from app_backend.shops.serializers import ShopSerializer


class ShopViewSet(viewsets.ModelViewSet):
    search_fields = ['name']
    filterset_fields = ['name']
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    queryset = Shop.objects.all().order_by('name')
    serializer_class = ShopSerializer
    permission_classes = [permissions.AllowAny]
    
