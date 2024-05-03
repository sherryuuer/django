from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Hello Universe")


def about(request):
    return HttpResponse("My name is Saaaally!")


def hello(request, first_name):
    return HttpResponse(f"Hello {first_name}")


def add_func(request, num1, num2):
    return HttpResponse(f"{num1 + num2}")
