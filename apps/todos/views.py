from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from apps.todos.models import Todo
from apps.todos.serializer import TodoSerializer

class TodoMixins(GenericViewSet,
                 mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 mixins.DestroyModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.RetrieveModelMixin):
    
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    search_fields = ['title', 'description']
    ordering_fields = ['created_at']
    ordering = ['-created_at']