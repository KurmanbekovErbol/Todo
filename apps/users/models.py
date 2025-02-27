from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(
        max_length=255,
        verbose_name="Имя пользователя"
    )
    email = models.EmailField(
        verbose_name="Адрес электронной почты"
    )
    phone_number = models.CharField(
        max_length=50,
        verbose_name='Номер телефона'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата регистрации"
    )
    age = models.IntegerField(
        verbose_name="Возраст"
    )
    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"