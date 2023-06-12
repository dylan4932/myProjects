from django.shortcuts import render
from django.http import HttpResponse
import os


def home(request):
    return render(request, 'home.html')


def hello(request):
    return HttpResponse('Hello World!')
