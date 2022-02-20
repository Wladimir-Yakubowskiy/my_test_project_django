from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    time_create = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
