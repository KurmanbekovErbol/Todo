from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название',
        unique=True
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    is_completed = models.BooleanField(
        primary_key=True,
        verbose_name='Завершено?'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата регистрации"
    )
    image = models.ImageField(
        upload_to='image/',
        verbose_name='Изображение'
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Таск"
        verbose_name_plural = "Таски"