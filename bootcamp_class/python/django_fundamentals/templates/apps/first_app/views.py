from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

# the index function is called when root is visited
def index(request):
    context = {
        "time": strftime("%b %d, %Y %H:%M %p", gmtime())
    }
    return render(request,'first_app/index.html', context)


# def timeDisplayFromUrls(request):
#     context = {
#         "somekey":"somevalue"
#     }
#     return render(request, "first_app/index.html", context)

def test(request):
    # form = request.method

    if request.method == "POST":
        print "*" * 50
        print request.POST
        print request.POST['name']
        request.session['name'] = request.POST['name']
        request.session['counter'] = 100
        print request.POST['description']
        request.session['name'] = "test"  # more on session below
        print "*" * 50
        return redirect("/")
    else:
        return redirect("/")

# Create your views here.
