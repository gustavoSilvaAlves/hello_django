from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello(request,nome,idade):
    return HttpResponse('<h1>Hello {} de {} anos </h1>'.format(nome,idade))