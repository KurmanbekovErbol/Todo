from django.contrib import admin
from apps.users.models import Users
# Register your models here.

@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone_number', 'age', 'created_at')