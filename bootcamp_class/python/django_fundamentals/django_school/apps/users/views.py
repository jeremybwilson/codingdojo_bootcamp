from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User
import re, bcrypt

# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your views here.
def new(request):

    if 'logged_in' not in request.session:
        request.session['logged_in'] = False

    print "*" * 80
    print request.session['logged_in']
    return render(request, 'users/new.html')

def create(request):
    if 'attempt_count' not in request.session:
        request.session['attempt_count'] = 0
    else:
        request.session['attempt_count'] += 1

    if request.method == 'POST':
            
        valid, result = User.objects.validate_and_create_user(request.POST)

        if not valid:
            for err in result:
                messages.error(err)
            return redirect('users:new')

        request.session['user_id'] = result
        print request.session['user_id']

        # if not 'users' in request.session:
        #     request.session['users'] = [user]
        # else:
        #     request.session['users'].append(user)
        #     request.session.modified = True

        # if 'user_id' not in request.session:
        #     user_id = False
        # else:
        #     user_id = request.session['users'][user_id]

        return redirect('dashboard:index')
    else:
        return redirect('users:new')

def show(request, user_id):
    print user_id, "This is the USER ID"
    user_id = int(user_id)
    user = request.session['users'][user_id]
    print user

    context = {
        'name': user['name'],
        'email': user['email'],
        'permission_level': user['permission_level'],
    }

    return render(request, 'users/show.html', context)