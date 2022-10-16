from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Takes request -> gives response
# It is a request handler

def calculate():
    x = 1
    y = 2

    return x + y

def say_hello(request):
    x = 1
    y = 2
    x = calculate()
    return render(request, 'hello.html')
    # return HttpResponse('Hello World!')
