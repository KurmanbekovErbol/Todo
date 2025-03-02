from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from apps.todos.models import Todo
from apps.todos.serializer import TodoSerializer

class UserMixins(GenericViewSet,
                 mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 mixins.DestroyModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.RetrieveModelMixin):
    
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer