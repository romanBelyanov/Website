from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from .models import Signin

def index(request):
    return render(request, 'home/index.html')

def signin(request):
    return render(request, 'home/signin.html')

def new_user(request):
    try:
        a = Signin.objects.get()
    except:
        return render(request, 'home/index.html')
    a.create(name=request.POST['name'], region=request.POST['region'], age=request.POST['age'], floor=request.POST['floor'], password=request.POST['password'], confirm_password=request.POST['confirm_password'])
    return HttpResponseRedirect(reverse('home:index'))