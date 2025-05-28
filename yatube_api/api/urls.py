from django.urls import include, path
from rest_framework import routers

from .viewsets import GroupViewSet, PostViewSet


router = routers.DefaultRouter()
router.register('groups', GroupViewSet)
router.register('posts', PostViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls.jwt')),
]
