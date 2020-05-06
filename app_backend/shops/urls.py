from django.urls import include, path
from rest_framework import routers
from app_backend.shops import views

app_name = "shops"

router = routers.DefaultRouter()
router.register(r'shops', views.ShopViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
