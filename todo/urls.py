"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from os import name
from django.contrib import admin
from django.urls import path
from main.views import homepage,test,meeting,add_todo,add_tomeet,habits,add_habits,delete_todo
from homework.views import homework,hw2
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage,name='home'),
    path('test', test, name="test"),
    path('hw',homework,name='homework'),
    path('hw2/',hw2,name='homework2'),
    path('meeting',meeting,name='meeting'),
    path('add todo/',add_todo,name='add todo'),
    path('add-tomeet/',add_tomeet,name='add-tomeet'),
    path('habits/',habits,name='habits'),
    path('add-habits/',add_habits,name='add-habits'),
    path('delete-todo/<id>',delete_todo,name='delete-todo'),
]   + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)\
    + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

    