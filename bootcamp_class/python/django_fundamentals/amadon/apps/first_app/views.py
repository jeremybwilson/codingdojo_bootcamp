from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):

    return render(request, 'first_app/index.html')

# Alternative front page route (redirect)
# def redirect(request):

#     return redirect("/amadon")

def process(request):

    # Case : initial condition setup
    if "total_number_of_transactions" not in request.session.keys():
        request.session["total_number_of_transactions"] = 0
        print request.session["total_number_of_transactions"]
    if "total_amount_history" not in request.session.keys():
        request.session["total_amount_history"] = 0
        print request.session["total_amount_history"]
    
    # checkout total price calculation based on product_id
    if request.POST["product_id"] == u"1":
        request.session["total_amount"] = 19.99 * int(request.POST['quantity'])
    elif request.POST['product_id'] == u"2":
         request.session["total_amount"] = 29.99 * int(request.POST['quantity'])
    elif request.POST['product_id'] == u"3":
         request.session["total_amount"] = 4.99 * int(request.POST['quantity'])
    elif request.POST['product_id'] == u"4":
         request.session["total_amount"] = 49.99 * int(request.POST['quantity'])

    # historical total amount calculation
    request.session['total_amount_history'] += request.session["total_amount"]

    # total transaction count
    request.session['total_number_of_transactions'] += 1

    return redirect('/amadon/checkout')

def checkout(request):
    context = {
        "total_amount" : request.session["total_amount"],
        "total_amount_history" : request.session["total_amount_history"],
        "total_number_of_transactions" : request.session["total_number_of_transactions"],
    }
    return render(request, 'first_app/show.html', context)

def reset(request):

    request.session.clear()
    return redirect('/')