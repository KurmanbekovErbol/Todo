# Generated by Django 5.1.5 on 2025-03-01 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='image',
            field=models.ImageField(default=1, upload_to='image', verbose_name='Изображение'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='TodoImage',
        ),
    ]
