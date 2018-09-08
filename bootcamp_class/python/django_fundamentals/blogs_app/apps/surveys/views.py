from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from models import *

# Create your views here.
# the index function is call when root is visited
def index(request):
    response = "Hello, I am the root of the survey application."
    return HttpResponse(response)

def new(request):
    
    return redirect('/')

def reset(request):
    request.session.clear()

    return redirect('/')