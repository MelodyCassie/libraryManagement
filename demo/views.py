from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def greet(request):
    return render(request, 'demo/hello.html', {'name': 'philip'})


def greet_me(request, name):
    return HttpResponse(f"let's explore django {name}")

