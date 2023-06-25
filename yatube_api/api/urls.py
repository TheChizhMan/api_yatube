from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.authtoken import views as auth_views
from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()
router.register('posts',
                PostViewSet,
                basename='posts')
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet,
                basename='comments')
router.register('groups',
                GroupViewSet,
                basename='groups')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/api-token-auth/', auth_views.obtain_auth_token, name='api_token_auth'),
]
