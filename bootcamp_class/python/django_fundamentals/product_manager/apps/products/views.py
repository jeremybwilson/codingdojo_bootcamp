# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
# from .models import Product
import re, bcrypt, json

# Create your views here.
def index(request):
    return render(request, 'products/index.html')

def new(request):
    pass

def create(request):
    pass

def show(request, user_id):
    pass

def edit(request, user_id):
    pass

def update(request, user_id):
    pass

def delete(request, user_id):
    pass

def logout(request):
  request.session.clear()
  return redirect('/')