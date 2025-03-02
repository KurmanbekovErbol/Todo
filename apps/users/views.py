from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from apps.users.models import Users
from apps.users.serializer import UserSerializer, RegisterUserSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

class UserMixins(GenericViewSet,
                 mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 mixins.DestroyModelMixin,
                 mixins.RetrieveModelMixin):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    search_fields = ['username']
    ordering_fields = ['created_at']
    ordering = ['-created_at']

    def get_serializer_class(self):
        if self.action in ('create', ):
            return RegisterUserSerializer
        return UserSerializer