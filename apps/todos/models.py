from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Тут должен быть название задачи",
        unique=True
    )
    description = models.TextField(
        verbose_name="Описание",
        help_text="Тут должен быть описание задачи"
    )
    is_completed = models.BooleanField(
        default=True,
        verbose_name="Завершон?"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
    )
    image = models.ImageField(
        upload_to='image',
        verbose_name='Изображение'
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

