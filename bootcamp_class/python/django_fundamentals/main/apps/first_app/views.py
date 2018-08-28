from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from models import *

# the index function is called when root is visited
def index(request):
    response = "Hello, I am your first request!"
    return HttpResponse(response)

def test(request):
    response = "Hello. I am test."
    return HttpResponse(response)

def special_case_2003(request):
    return HttpResponse("special_case_2003 method")

def show(request, number):
    print number
    return HttpResponse("show method " + number)

def show_word(request, word):
    return HttpResponse("show_word method " + word)

def year_archive(request, year):
    return HttpResponse("year_archive method " + year)

def month_archive(request, year, month):
    return HttpResponse("month_archive method " + year + month)

# Create your views here.
