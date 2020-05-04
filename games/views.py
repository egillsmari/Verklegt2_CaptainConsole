from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(requeste):
    return HttpResponse('<h2> Bunch of games </h2>')