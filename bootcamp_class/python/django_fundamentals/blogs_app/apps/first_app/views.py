from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from models import *

# the index function is call when root is visited
def index(request):
    response = "Hello, I am the root of the site."
    return HttpResponse(response)

def blogs_app(request):
    response = "Hello, I am the blog application."
    return HttpResponse(response)

def new(request):
    response = "Hello, I am the new route."
    return HttpResponse(response)

def create(request):
    response = "Hello, I am the create route."
    return HttpResponse(response)

def show(request, number):
    print number
    return HttpResponse("Hello, I am the placeholder to display blog number: " + number)

def edit(request, number):
    print number
    return HttpResponse("Hello, I am the placeholder to edit blog number: " + number)

def destroy(request, number):
    print number
    # return HttpResponse("Hello, I am the placeholder to display blog {# number #} route. " + number)
    return redirect('/')

# Create your views here.