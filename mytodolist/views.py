from django.shortcuts import render, redirect
from .models import Task

# Create your views here.

def index(request):
    tasks = Task.objects.all()
    if request.method == 'POST':
        new_url = Task(title = request.POST['title'])
        new_url.save()
        return redirect('/')
    return render(request, 'index.html', {'tasks':tasks})

def delete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('/')


