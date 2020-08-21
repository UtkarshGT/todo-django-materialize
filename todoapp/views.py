from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView,DeleteView

from .models import Task
from .forms import TaskForm


# used function based view to pass multiple context
# TODO: add due_date and completed indicator

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


class TaskDetailView(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = "todoapp/detail.html"


# TODO: add Materialize CSS to elements, this uses modelform by default
# TODO: adding due date later doesn't work

class TaskUpdateView(UpdateView):
    model = Task
    fields = '__all__'
    template_name = "todoapp/update.html"

    # reverse doesn't work with class based views, equivalent is reverse_lazy
    success_url = reverse_lazy('todoapp:index')


class TaskDeleteView(DeleteView):
    model = Task
    context_object_name = 'blog_delete'
    template_name = "todoapp/delete.html"
    
    success_url = reverse_lazy('todoapp:index')