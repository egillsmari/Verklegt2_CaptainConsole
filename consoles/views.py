from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(requeste):
    return HttpResponse('<h1>Here will be many consoles<h1>')
