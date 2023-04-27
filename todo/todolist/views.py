from django.shortcuts import render,redirect
from django.views.generic.list import ListView
from .models import Task
from django.urls import reverse_lazy
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
)
# Create your views here.

from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class TaskList(LoginRequiredMixin , ListView):
    model = Task
    context_object_name = 'tasks'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)
    

class AddTask(LoginRequiredMixin ,CreateView ):
    model = Task
    fields = ["title"]

    success_url = reverse_lazy("tasks:task_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddTask, self).form_valid(form)
    

class UpdateTask(LoginRequiredMixin , UpdateView):
    model = Task
    success_url = reverse_lazy("tasks:task_list")
    fields = ["title"]
    template_name = 'todolist/update_task.html'


class TaskDelete(LoginRequiredMixin , DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:task_list")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)
    

class DoneTask(LoginRequiredMixin ,View):
    model = Task
    success_url = reverse_lazy("tasks:task_list")

    def get(self , request,*args, **kwargs):
        object  = Task.objects.get(id = kwargs.get('pk'))
        object.complete = True
        object.save()
        return redirect(self.success_url)