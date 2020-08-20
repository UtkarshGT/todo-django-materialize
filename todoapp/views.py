from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView,DeleteView

from .models import Task
from .forms import TaskForm



def index(request):
    tasklist = Task.objects.all()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            Task.objects.create(**form.cleaned_data)

    form = TaskForm()

    context = {
        'tasklist': tasklist,
        'form': form
    }
    return render(request, 'todoapp/index.html', context)




# class TaskListView(ListView):
#     model = Task
#     context_object_name = 'tasklist'
#     template_name = "todoapp/index.html"



class TaskDetailView(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = "todoapp/detail.html"


class TaskUpdateView(UpdateView):
    model = Task
    fields = '__all__'
    template_name = "todoapp/update.html"

    success_url = reverse_lazy('todoapp:index')

class TaskDeleteView(DeleteView):
    model = Task
    context_object_name = 'blog_delete'
    template_name = "todoapp/delete.html"

    success_url = reverse_lazy('todoapp:index')


def add_view(request):

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            Task.objects.create(**form.cleaned_data)
            return redirect('/')
    else:
        form = TaskForm()

    context = {
        'form': form
    }
    return render(request, 'todoapp/add.html', context)