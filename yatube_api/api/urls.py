from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, UserViewSet

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('v1/auth/', include('djoser.urls')),
    path('v1/auth/', include('djoser.urls.jwt')),
    path('v1/', include(router.urls)),
]
