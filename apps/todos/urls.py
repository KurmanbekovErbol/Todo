from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.todos.views import UserMixins

router = DefaultRouter()
router.register('todo', UserMixins, basename='todos')


urlpatterns = router.urls