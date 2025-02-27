from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.users.views import UserMixins

router = DefaultRouter()
router.register('user', UserMixins, basename='users')

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='api/login'),
    path('refresh/', TokenRefreshView.as_view(), name='api/refresh')
]

urlpatterns += router.urls