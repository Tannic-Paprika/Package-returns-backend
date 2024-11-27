# returns/urls.py
from django.urls import path, include
from rest_framework import routers
from .views import ReturnViewSet

router = routers.DefaultRouter()
router.register(r'returns', ReturnViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
