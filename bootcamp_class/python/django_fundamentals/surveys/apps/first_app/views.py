from django.shortcuts import render, redirect

# Create your views here.
def index(request):

    print '*' * 80
    print 'hello'
    return render(request, 'first_app/index.html')

def process(request):

    return redirect('/')

def results(request):

    return render(request, 'first_app/results.html')