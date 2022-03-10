from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    description = models.TextField(max_length=1000, verbose_name='Описание')
    time_create = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовать')

    def __str__(self):
        return self.title
