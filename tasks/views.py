# tasks/views.py
from django.shortcuts import render, redirect
from .models import Task

def index(request):
    if request.method == 'POST':
        if 'delete' in request.POST:
            task_id = request.POST.get('delete')
            Task.objects.filter(id=task_id).delete()
        else:
            title = request.POST.get('title')
            if title:
                Task.objects.create(title=title)
        return redirect('/')

    tasks = Task.objects.all().order_by('-created_at')  # orden descendente
    return render(request, 'tasks/index.html', {'tasks': tasks})
