from django.contrib import admin
from apps.todos.models import Todo
from apps.todos.forms import TodoForm
# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    form = TodoForm
    list_display = ('title', 'is_completed', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('is_completed', 'created_at')
    ordering = ('created_at',)


admin.site.register(Todo, TodoAdmin)