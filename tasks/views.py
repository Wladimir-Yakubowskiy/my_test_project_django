from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseServerError
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView

from tasks.forms import *
from tasks.models import Task


def add_task(request):
    form = AddTaskForm()
    return render(request, 'tasks/add_task.html', {'form': form, 'title': 'Добавление статьи'})


class TasksIndex(ListView):
    model = Task
    template_name = 'tasks/index.html'
    context_object_name = 'tasks'  # передающиеся в шаблон данные (object_list по умолчанию)
    extra_context = {'title': 'Главная страница'}  # статические неизменяемые данные

    def get_queryset(self):
        return Task.objects.filter(is_published=True)


class ShowTask(DetailView):
    model = Task
    template_name = 'tasks/task.html'
    pk_url_kwarg = 'id'


def pageNotFound(request, exeption):
    print('404 сработала')
    return HttpResponseNotFound('Страница не найдена')


def serverError(request):
    print('500 сработала')
    return HttpResponseServerError('Ошибка на сервере')
