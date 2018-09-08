from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import *

from django.views.generic import TemplateView
from forms import HomeForm

class HomeView(TemplateView):
    template_name = 'blogs/index.html'
    print "This is the HomeView class being called."

    # Create your views here.
    def index(request):
        print "Hello, I am the root of the site."
        return render(request, self.template_name)

    def blogs(request):
        print "Hello, I am the blog application."
        return render(request, self.template_name)

    def get(self, request):
        form = HomeForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['post']

        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)

    def new(request):
        response = "Hello, I am the new route."
        return HttpResponse(response)

    def show(request):
        print "This is the show form post results route"
        return render(request, self.template_name)

    def edit(request, number):
        print number
        return HttpResponse("Hello, I am the placeholder to edit blog number: " + number)

    def destroy(request, number):
        print number
        # return HttpResponse("Hello, I am the placeholder to display blog {# number #} route. " + number)
        return redirect('/')

    def reset(request):
        request.session.clear()
        return redirect('/')