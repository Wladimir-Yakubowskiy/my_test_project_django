from django.urls import path, include
from .views import *

app_name = 'my_app'

urlpatterns = [
    path('index/', TasksIndex.as_view(), name='index'),
    path('tasks/<int:id>/', ShowTask.as_view(), name='my_task'),
    path('save-form/', SaveTask.as_view(), name='save_task'),
    path('add_task', add_task, name='add_task'),
    path('delete/<int:task_id>/', delete, name='delete'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
]
