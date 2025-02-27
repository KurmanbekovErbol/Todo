from rest_framework import serializers
from apps.users.models import Users

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
        if '+996' not in attrs['phone_number']:
            raise serializers.ValidationError({'phone_number': 'Номер телефона должен быть в формате +996ХХХХХХХХХ'})
        if len(attrs['phone_number']) != 13:
            raise serializers.ValidationError({'phone_number': 'Некорректный номер телефона. Попробуйте ещё раз'})
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