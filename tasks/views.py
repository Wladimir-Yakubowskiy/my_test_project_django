from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseServerError, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView

from tasks.forms import *
from tasks.models import Task


def add_task(request):
    form = AddTaskForm()
    return render(request, 'tasks/add_task.html', {'form': form, 'title': 'Добавление статьи'})


def delete(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return HttpResponseRedirect(reverse('my_app:index'))


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'tasks/register.html'
    success_url = reverse_lazy('my_app:index')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'tasks/authentication.html'

    def get_success_url(self):
        return reverse_lazy('my_app:index')


# Класс для обработки входящего запроса
class SaveTask(View):
    def post(self, request, *args, **kwargs):
        # Заранее предупреждаем, какая именно форма придет
        form = AddTaskForm(request.POST or None)
        # Если все данные в форме валидны, то...
        if form.is_valid():
            # Создаем экземпляр объекта по нашей форме
            new_task = form.save(commit=False)
            # Заполняем поля объекта
            new_task.title = form.cleaned_data['title']
            new_task.description = form.cleaned_data['description']
            # Сохраняем объект после изменений
            new_task.save()
            # Возвращаем на страницу, с которой была отправлена форма
        return HttpResponseRedirect(reverse('my_app:index'))


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
