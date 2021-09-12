from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Product

def index(request):
    if request.method == "POST":
        the_name = request.POST.get("name")

        Product.objects.create(name=the_name)

        return redirect(reverse_lazy("display"))
    else:
        return render(request, "base.html")


def display(request):
    query_set = Product.objects.all()

    return render(request, "display.html", {'all': query_set})


def vote(request):
    if request.method == "POST":
        
        query_set = Product.objects.all()
        for another in query_set:
            if request.POST.get('p' + str(another.id)) == 'vote':
                another.vote += 1
                another.save()
           
        return redirect(reverse_lazy("vote"))
        
    else:
        query_set = Product.objects.all()
        return render(request, "vote.html", {'all':query_set})