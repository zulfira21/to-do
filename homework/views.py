from django.shortcuts import render,HttpResponse

# Create your views here.
def homework(request):
    return render(request,'hw.html')

def hw2(request):
    return HttpResponse('Добро пожаловать в приложение ToDo ')

