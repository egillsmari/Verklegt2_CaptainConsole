from django.shortcuts import render


# Create your views here.

def index(requeste):
    return render(requeste, 'homepage/index.html')
