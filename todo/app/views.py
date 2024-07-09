from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


from .rabbitmq import publish_message

def index(request):
    # publish_message('Message here!')
    # return HttpResponse("Hello, world. You're at the todo index. RabbitMQ")
    return render(request, 'index.html')

from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Task
from .forms import TaskForm, TeamForm

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'app/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'app/add_task.html', {'form': form})

def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'app/task_detail.html', {'task': task})


def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_detail', task_id=task.id)
    else:
        form = TaskForm(instance=task)
    return render(request, 'app/edit_task.html', {'form': form})


def today_tasks(request):
    today = timezone.now().date()
    tasks = Task.objects.filter(due_date=today)
    return render(request, 'app/today_tasks.html', {'tasks': tasks})

def upcoming_tasks(request):
    today = timezone.now().date()
    tasks = Task.objects.filter(due_date__gt=today)
    return render(request, 'app/upcoming_tasks.html', {'tasks': tasks})

def profile(request):
    return render(request, 'app/profile.html', {'user': request.user})

def add_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            # Process the form data here
            return redirect('task_list')
    else:
        form = TeamForm()
    return render(request, 'app/add_team.html', {'form': form})
