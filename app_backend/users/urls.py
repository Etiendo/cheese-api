from django.urls import include, path
from rest_framework import routers
from app_backend.users import views

app_name = "users"

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
