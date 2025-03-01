from rest_framework import serializers
from apps.todos.models import Todo
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'is_completed', 'created_at', 'image']

