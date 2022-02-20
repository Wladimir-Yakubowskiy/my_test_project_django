from django import forms
from .models import *


class AddTaskForm(forms.Form):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    is_published = models.BooleanField()
