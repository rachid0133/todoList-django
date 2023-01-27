from django.shortcuts import render, redirect
from .models import Task
from datetime import datetime

# Create your views here.

def index(request):

    tasks = Task.objects.all()
    title = request.POST.get('title')
    times = request.POST.get('time')
    # my_time = datetime.strptime(times, '%H:%M').time()
    # print(times)
    if request.method == 'POST':
        new_url = Task(title=title, time=times)
        new_url.save()
        return redirect('/')
    return render(request, 'index.html', {'tasks':tasks})

def delete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('/')


