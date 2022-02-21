from django.urls import path
from .views import *

app_name = 'my_app'

urlpatterns = [
    path('index/', TasksIndex.as_view(), name='index'),
    path('tasks/<int:id>/', ShowTask.as_view(), name='my_task'),
    path('save-form/', SaveTask.as_view(), name='save_task'),
    path('', add_task, name='add_task')
]
