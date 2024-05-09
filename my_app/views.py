from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView, CreateView
from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return render(request, 'my_app/index.html', {})
