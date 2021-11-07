from django.http.response import HttpResponseNotModified
from django.shortcuts import render,HttpResponse,redirect
from .models import ToDo
from .models import ToMeet


def homepage(request):
    return render(request, "index.html")

def test(request):
    todo_list = ToDo.objects.all()
    return render(request,"test.html",{"todo_list":todo_list})

def meeting(request):
    meeting_list = ToMeet.objects.all()
    return render(request,"meeting.html",{"meeting_list":meeting_list})

def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    
    return redirect(test)