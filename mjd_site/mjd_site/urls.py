"""
URL configuration for mjd_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import home.views, food.views, hotel.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.views.index, name='index'),
    path('signin/', home.views.signin, name='signin'),
    path('new_user/', home.views.new_user, name='new_user'),
    path('done/', home.views.done, name='done'),
    path('login/', home.views.login, name='login'),
    path('entrance/', home.views.entrance, name='entrance'),
    path('map/', food.views.map, name='map'),
    path('hotel/', hotel.views.hotel_, name='hotel'),
    path('<str:name>/', include('home.urls')),
]
