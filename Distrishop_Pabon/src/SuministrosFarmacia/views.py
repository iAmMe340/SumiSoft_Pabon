from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render 


# Create your views here.
from django.http import HttpResponse


# def index(request):
 #   return HttpResponse("Hello, world. You're at the farmacy ammo index.")

def index(request):
    return render(request, 'index.html', {}) 

