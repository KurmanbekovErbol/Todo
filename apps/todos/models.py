from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from apps.utils import get_todo_upload_path

# Create your models here.

class Todos(models.Model):
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
    def __str__(self):
        return self.title
    
    def get_first_image(self) -> 'TodoImage':
        todo_image = TodoImage.objects.filter(todo=self).first()
        return todo_image.image.url if todo_image else None
    
    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

class TodoImage(models.Model):
    todo = models.ForeignKey(
        to="todo",
        on_delete=models.CASCADE,
        verbose_name="Задание",
        related_name="todo_image"
    )
    image = ProcessedImageField(
        upload_to=get_todo_upload_path,
        verbose_name="Изображение",
        processors=[ResizeToFill(100,50)],
        format='webp',
        options={'quality': 100}
    )
    position = models.PositiveIntegerField(
        default=0,
        blank=True, null=True
    )
    def __str__(self):
        return str(self.image.name)
    
    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        ordering = ['position',]