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

def edit(request,pk):
    note = Notes.objects.get(id=pk)
    previous_title = note.title
    prev_description = note.description
    if request.method == 'POST':
        new_title = request.POST['title']
        new_description = request.POST['description']
        note.title = new_title
        note.description = new_description
        note.save()
        return redirect('home')
    obj = Notes.objects.all()
    context = {'tasks':obj , 'title':previous_title , 'description': prev_description}
    return render(request,'home.html',context)

def delete(request,pk):
    # if request.method == 'POST':
        note = Notes.objects.get(id = pk)
        note.delete()
        return redirect('home')