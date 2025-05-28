from django.urls import include, path
from rest_framework import routers

from .viewsets import GroupViewSet


router = routers.DefaultRouter()
router.register('groups', GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls.jwt')),
]
