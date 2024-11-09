from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from .models import Signin


def index(request):
    return render(request, 'home/index.html')

def signin(request):
    return render(request, 'home/signin.html')

def done(request):
    return render(request, 'home/done.html')

def new_user(request):
    try:
        a = Signin.objects.get(name=request.POST['name'])
        if request.POST['name'] in a.name:
            return render(request, 'home/signin_name.html', {'name_': request.POST['name'], 'region': request.POST['region'], 'age': request.POST['age'], 'floor': request.POST['floor'], 'password': request.POST['password'], 'confirm_password': request.POST['confirm_password']})
    except:
        pass
    if request.POST['password'] == request.POST['confirm_password']:
        Signin.objects.create(name=request.POST['name'], region=request.POST['region'], age=request.POST['age'],
                      floor=request.POST['floor'], password=request.POST['password'],
                      confirm_password=request.POST['confirm_password'])
    else:
        return render(request, 'home/signin_password.html', {'name_': request.POST['name'], 'region': request.POST['region'], 'age': request.POST['age'], 'floor': request.POST['floor'], 'password': request.POST['password'], 'confirm_password': request.POST['confirm_password']})
    return redirect('http://127.0.0.1:8000/done')

def login(request):
    return render(request, 'home/login.html')


def entrance(request):
    try:
        a = Signin.objects.get(name = request.POST['name'])
        if a.password == request.POST['password']:
            return redirect('http://127.0.0.1:8000/')
        else:
            return render(request, 'home/login_password.html', context={'name_': request.POST['name']})
    except:
        return render(request, 'home/login_name.html')