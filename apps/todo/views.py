from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from apps.todo.models import Todo
from apps.todo.serializer import TodoSerializer

class TodoMixins(GenericViewSet,
                 mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 mixins.DestroyModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer