from rest_framework import serializers
from apps.users.models import Users
import re

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'username', 'email', 'phone_number', 'created_at', 'age', 'is_active')

class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length = 50,
        write_only = True
    )
    confirm_password = serializers.CharField(
        max_length = 50,
        write_only = True
    )
    class Meta:
        model = Users
        fields = ('id', 'username', 'email', 'phone_number', 'created_at', 'age', 'is_active', 'password', 'confirm_password')

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({'confirm_password': 'Пароли отличаются'})
        
        if len(attrs['password']) < 8:
            raise serializers.ValidationError({"password": 'Пароль должен быть не менее 8 символов'})
        
        # Очистка номера от пробелов
        phone_number = attrs['phone_number'].replace(" ", "").strip()

        # Проверка начала номера
        if not phone_number.startswith('+996'):
            raise serializers.ValidationError({'phone_number': 'Номер должен начинаться с +996'})

        # Регулярное выражение для проверки формата номера (+996XXXXXXXXX)
        phone_pattern = r'^\+996\d{9}$'
        if not re.fullmatch(phone_pattern, phone_number):
            raise serializers.ValidationError({'phone_number': 'Некорректный номер. Формат: +996XXXXXXXXX'})

        # Обновляем номер телефона в атрибутах
        attrs['phone_number'] = phone_number
        return attrs
    
    def create(self, values):
        user = Users.objects.create(
            username=values['username'],
            email=values['email'],
            phone_number=values['phone_number'],
            age=values['age']
        )
        user.set_password(values['password'])
        user.save()
        return user