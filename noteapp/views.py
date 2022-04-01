from asyncio import Task, tasks
from email import message
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Notes
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
# from django.contrib.auth.decorators import login_required

def home(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            input1 = request.POST['title']
            input2 = request.POST['description']
            Notes.objects.create(title = input1 , description = input2 )
            messages.success(request,'Note Added Successfully..')
            return redirect('home')
        obj = Notes.objects.all()
        context = {'tasks':obj , 'login': True}
        return render(request , 'home.html',context)
    else:
        return render(request , 'home.html')


def edit(request,pk):
    if request.user.is_authenticated:
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
    else:
        return redirect('login')


def delete(request,pk):
    if request.user.is_authenticated:
        # if request.method == 'POST':
            note = Notes.objects.get(id = pk)
            note.delete()
            return redirect('home')
    else:
        return redirect('login')

def logout_user(request):
    logout(request)
    return redirect('login')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pswd']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'Login successful')
            return redirect('home')

        else:
            messages.error(request,'Username or Password is Incorrect. Please give coreect one')
    return render(request,'login.html')