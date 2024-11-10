from django.shortcuts import render
from home.models import Signin
from django.http import Http404

def map(request):
    return render(request, 'food/map.html')

def map_for_authorise(request, name):
    try:
        a = Signin.objects.get(name=name)
    except:
        raise Http404()

    return render(request, 'food/map_for_authorise.html', {'obj': a, 'http1': f'http://127.0.0.1:8000/{a.name}/profile', 'http2': f'http://127.0.0.1:8000/{a.name}', 'http3': f'http://127.0.0.1:8000/{a.name}/map', 'http4': f'http://127.0.0.1:8000/{a.name}/hotel', 'http5': f'http://127.0.0.1:8000/{a.name}/buy'})
