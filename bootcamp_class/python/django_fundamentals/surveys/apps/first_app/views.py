from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

# Create your views here.
def index(request):
    # print '*' * 80
    # print 'hello'

    if 'name' not in request.session:
        request.session['name'] = 'No name entered'
    if 'location' not in request.session:
        request.session['location'] = 'No location entered'
    if 'language' not in request.session:
        request.session['language'] = 'No language chosen'
    if 'comments' not in request.session:
        request.session['comments'] = 'No comments entered'

    return render(request, 'first_app/index.html')

def process(request):

    if 'session_count' not in request.session:
        request.session['session_count'] = 0
    else:
        request.session['session_count'] += 1
        print request.session['session_count']

    if request.method == 'GET':

        errors = []
        print '*' * 80
        print "Here are the form results: ", request.GET
        name = request.GET['name']
        request.session['name'] = name
        location = request.GET['location']
        request.session['location'] = location
        language = request.GET['language']
        request.session['language'] = language
        comments = request.GET['comments']
        request.session['comments'] = comments
        print name, location, language, comments

        if len(request.GET['name']) < 1:
            errors.append('Name cannot be blank.')

        if len(request.GET['comments']) < 1:
            errors.append('Comments field cannot be blank.')

        if len(errors) > 0:
            for error in errors:
                messages.error(request, error)
            return redirect('/')
        
        print '*' * 80
        return redirect('/results')

    # else:
    #     return redirect('/')

    # if len(request.POST['name']) > 0:
    #     request.session['name'] = request.POST['name']
 
    # if request.session['location'] != '':
    #     request.session['location'] = request.POST['location']

    # if request.session['language'] != '':
    #     request.session['language'] = request.POST['language']

    # if len(request.POST['comments']) > 0:
    #     request.session['comments'] = request.POST['comments']

    # return redirect('/')

def results(request):

    return render(request, 'first_app/results.html')