from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):

    return render(request, 'first_app/index.html')

def attempt(request):
    
    if 'session_attempt' not in request.session:
        request.session['session_attempt'] = 0
    else:
        request.session['session_attempt'] += 1
        print request.session['session_attempt']

    if 'random_word' not in request.session:
        print "*" * 80
        print request.session['random_word']
    else:
        request.session['random_word'] = get_random_string(length=14)
        return redirect('/')    

    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')