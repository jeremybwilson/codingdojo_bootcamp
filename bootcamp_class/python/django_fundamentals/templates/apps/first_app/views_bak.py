from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string

from models import *

# the index function is called when root is visited
def index(request):
    # anything you did in the shell you can insert here
    print strftime("%Y-%m-%d %H:%M:%S", gmtime())
    print get_random_string(length=14)
    print "Hello, first request here."

    return render(request, 'first_app/index.html', {"blogs": Blogs.objects.all() })

def new(request):
    return render(request, 'first_app/new.html')

def show(request, id):
    return render(request, 'first_app/show.html', {"blog": Blog.objects.get(id=10)})

def edit(request, id):
    return render(request, 'first_app/edit.html', {"blog: Blog.ojects.get(id=10)"})

def update(request, id):
    errors = Blob.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors, iteritems():

# Create your views here.
