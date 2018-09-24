# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Course

# Create your views here.
def index(request):
    context = {
        "courses" : Course.objects.all(),
    }

    return render(request, "courses/index.html", context)

def add(request):
    if request.method == 'POST':

        valid, result = Course.objects.custom_form_validator(request.POST)

        if valid:
            request.session['course_id'] = result
            # Course.objects.create(name = request.POST["course_name"], description = request.POST["desc"])
            return redirect('courses:index')
        else:
            for error in result:
                messages.error(request, error)
            return redirect('courses:index')
    else:
        return redirect('courses:new')

def confirm(request, course_id):
    context = {
        'course' : Course.objects.get(id=course_id)
    }

    return render(request, "courses/confirm.html", context)

def destroy(request, course_id):
    Course.objects.get(id=course_id).delete()

    return redirect("/")