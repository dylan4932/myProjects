from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
import os


def home(request):
    return render(request, 'home.html')


def hello(request):
    return HttpResponse('Hello World!')

@api_view(['GET'])
def getData(request):
    person = {'name': 'Dennis', 'age': 28}
    return HttpResponse(person)
