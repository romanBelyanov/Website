from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from pkg_resources.extern import names

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
            return render(request, 'home/signin_name.html', {'name_': request.POST['name'], 'region': request.POST['region'], 'age': request.POST['age'], 'floor': request.POST['floor'], 'height': request.POST['height'], 'weight': request.POST['weight'], 'password': request.POST['password'], 'confirm_password': request.POST['confirm_password']})
    except:
        pass
    if request.POST['password'] == request.POST['confirm_password']:
        Signin.objects.create(name=request.POST['name'], region=request.POST['region'], age=request.POST['age'],
                      floor=request.POST['floor'], height=request.POST['height'], weight=request.POST['weight'],  password=request.POST['password'],
                      confirm_password=request.POST['confirm_password'])
    else:
        return render(request, 'home/signin_password.html', {'name_': request.POST['name'], 'region': request.POST['region'], 'age': request.POST['age'], 'floor': request.POST['floor'], 'height': request.POST['height'], 'weight': request.POST['weight'], 'password': request.POST['password'], 'confirm_password': request.POST['confirm_password']})
    return redirect('http://127.0.0.1:8000/done')

def login(request):
    return render(request, 'home/login.html')



def entrance(request):
    try:
        a = Signin.objects.get(name = request.POST['name'])
        if a.password == request.POST['password']:
            return redirect(f'http://127.0.0.1:8000/{request.POST["name"]}')
        else:
            return render(request, 'home/login_password.html', context={'name_': request.POST['name']})
    except:
        return render(request, 'home/login_name.html')

def open_lk(request, name):
    try:
        a = Signin.objects.get(name=name)
    except:
        raise Http404()

    return render(request, 'home/lk.html', {'obj': a, 'http1': f'http://127.0.0.1:8000/{a.name}/profile', 'http2': f'http://127.0.0.1:8000/{a.name}', 'http3': f'http://127.0.0.1:8000/{a.name}/map', 'http4': f'http://127.0.0.1:8000/{a.name}/hotel', 'http5': f'http://127.0.0.1:8000/{a.name}/buy'})
def profile(request, name):
    try:
        a = Signin.objects.get(name=name)
    except:
        raise Http404()

    return render(request, 'home/profile.html', {'obj': a, 'http1': f'http://127.0.0.1:8000/{a.name}/profile', 'http2': f'http://127.0.0.1:8000/{a.name}', 'http3': f'http://127.0.0.1:8000/{a.name}/map', 'http4': f'http://127.0.0.1:8000/{a.name}/hotel', 'http5': f'http://127.0.0.1:8000/{a.name}/buy'})
