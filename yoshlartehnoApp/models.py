from django import forms
from django.db import models
from django.forms import ValidationError
from embed_video.fields import EmbedVideoField
# Create your models here.


class Project(models.Model):
    img = models.ImageField('Фотография', upload_to='project_img/')

class Video(models.Model):
    title = models.CharField('Название Видео', max_length=50, unique=True)
    description = models.TextField('Информация')
    video_file = EmbedVideoField()
    create_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        # Проверяем, существует ли уже запись в модели
        if Video.objects.exists():
            # Если существует, игнорируем создание новой записи
            return
        # Если записи не существует, создаем новую запись
        super().save(*args, **kwargs)
