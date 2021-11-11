from django.http.response import HttpResponseNotModified
from django.shortcuts import render,HttpResponse,redirect
from .models import ToDo
from .models import ToMeet
from .models import Habits



def homepage(request):
    return render(request, "index.html")

def test(request):
    todo_list = ToDo.objects.all()
    return render(request,"test.html",{"todo_list":todo_list})

def meeting(request):
    meeting_list = ToMeet.objects.all()
    return render(request,"meeting.html",{"meeting_list":meeting_list})

def habits(request):
    habits_list = Habits.objects.all()
    return render(request,"habits.html",{"habits_list":habits_list})



    

def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(test)


def add_tomeet(request):
    form = request.POST
    text = form["tomeet_text"]
    tomeet = ToMeet(person=text)
    tomeet =ToMeet(phone_Number=text)
    tomeet.save()
    return redirect(meeting)

def add_habits(request):
    form = request.POST
    text = form["habits_text"]
    habits = Habits(name=text)
    habits.save()
    return redirect(habits)

def delete_todo(request,id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)

def mark_todo(request,id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = True
    todo.save()
    return redirect(test)

def delete_tomeet(request,id):
    tomeet = ToMeet.objects.get(id=id)
    tomeet.delete()
    return redirect(meeting) 

def mark_tomeet(request,id):
    tomeet = ToMeet.objects.get(id=id)
    tomeet.is_favorite = True
    tomeet.save()
    return redirect(meeting)

def mark_undo_todo(request,id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = False
    todo.save()
    return redirect(test)

def close_todo(request,id):
    todo =ToDo.objects.get(id=id)
    todo.is_closed = not todo.is_closed
    todo.save()
    return redirect(test)
    