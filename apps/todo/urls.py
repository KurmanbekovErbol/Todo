from rest_framework.routers import DefaultRouter
from apps.todo.views import TodoMixins

router = DefaultRouter()

router.register(r'todo', TodoMixins, basename='todos')

urlpatterns = router.urls