from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# redirects user to a certain part of our page 
from django.urls import reverse_lazy

from .models import Task
# Create your views here.

# creating TaskList to see a list of all tasks to be done
class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'

# creating TaskDetail so when you click in you can see the page of task details
class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'

# creating class to create tasks
class TaskCreate(CreateView):
    model = Task
    # easier way to list out than having to create a list of all fields
    fields = '__all__'
    # if everything goes well, send user back to list
    success_url = reverse_lazy('tasks')

class TaskUpdate(UpdateView):
    model = Task
    # easier way to list out than having to create a list of all fields
    fields = '__all__'
    # if everything goes well, send user back to list
    success_url = reverse_lazy('tasks')

class DeleteView(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')

