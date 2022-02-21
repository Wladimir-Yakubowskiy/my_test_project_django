from django import forms
from .models import *


class AddTaskForm(forms.ModelForm):

    class Meta:
        # Указываем, в какую модель из models.py будем все это сохранять
        model = Task
        # тут список полей, которые нужно вывести. Поля соответствуют полям модели из models.py
        fields = (
            'title', 'description', 'is_published'
        )
