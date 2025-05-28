from django.urls import include, path
from rest_framework import routers

from .viewsets import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet


router = routers.DefaultRouter()
router.register('groups', GroupViewSet)
router.register('posts', PostViewSet)
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)
router.register('follow', FollowViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls.jwt')),
]
