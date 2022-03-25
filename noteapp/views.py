from asyncio import Task, tasks
from multiprocessing import context
from django.shortcuts import redirect, render
from .models import Notes

# Create your views here.

def home(request):
    if request.method == 'POST':
        input1 = request.POST['title']
        input2 = request.POST['description']
        Notes.objects.create(title = input1 , description = input2 )
        return redirect('home')
    obj = Notes.objects.all()
    context = {'tasks':obj}
    return render(request , 'home.html',context)
