from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from models import *

# Create your views here.
# the index function is call when root is visited
def index(request):
    response = "Hello, I am the root of the users application."
    return HttpResponse(response)

def login(request):
    response = "Hello, I am the login route."
    return redirect('/')

def new(request):
    response = "Hello, I am the new user route."
    return redirect('/')

def register(request):
    response = "Hello, I process the new user form."
    return redirect('/')

def reset(request):
    request.session.clear()

    return redirect('/')