from django.shortcuts import render, redirect
from .models import Task
from django.utils.timezone import now

def index(request):
    filter_option = request.GET.get("filter", "all")

    if request.method == "POST":
        if "title" in request.POST:
            Task.objects.create(title=request.POST["title"])
        elif "delete" in request.POST:
            Task.objects.filter(id=request.POST["delete"]).delete()
        elif "toggle" in request.POST:
            task = Task.objects.get(id=request.POST["toggle"])
            task.completed = not task.completed
            task.save()
        elif "edit_id" in request.POST:
            task = Task.objects.get(id=request.POST["edit_id"])
            task.title = request.POST["edit_title"]
            task.save()
        return redirect("/")

    if filter_option == "completed":
        tasks = Task.objects.filter(completed=True).order_by("-created_at")
    elif filter_option == "pending":
        tasks = Task.objects.filter(completed=False).order_by("-created_at")
    else:
        tasks = Task.objects.all().order_by("-created_at")

    return render(request, "tasks/index.html", {"tasks": tasks, "filter": filter_option})
