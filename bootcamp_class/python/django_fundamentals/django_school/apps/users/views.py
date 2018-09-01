from django.shortcuts import render, redirect
from django.contrib import messages
import re

# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your views here.
def new(req):
    return render(req, 'users/new.html')

def create(req):
    errors = []

    if len(req.POST['name']) < 1:
        errors.append('Name cannot be blank.')
    if len(req.POST['name']) < 2:
        errors.append('Name must be longer than 2 characters.')
    if len(req.POST['email']) < 1:
        errors.append('Email cannot be blank.')
    elif not EMAIL_REGEX.match(req.POST['email']):
        errors.append('You must enter a valid email address!')
    if len(req.POST['password']) < 1:
        errors.append('Password cannot be blank.')
    if len(req.POST['password']) < 3:
        errors.append('Password must be at least 3 characters long.')
    if len(req.POST['confirm_password']) < 1:
        errors.append('Confirm password cannot be blank.')
    if req.POST['password'] != req.POST['confirm_password']:
        errors.append('Passwords do not match!')

    if len(errors) > 0:
        for error in errors:
            messages.error(req, error)
        return redirect('/users/new')
    # if all error validations cleared, then success
    # else:
    #     return redirect('/')
        
    return redirect('/')