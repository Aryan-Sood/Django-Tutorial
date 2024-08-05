from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    people = [
        {'name': 'Aryan', 'age': 22},
        {'name': 'Sid', 'age': 9},
        {'name': 'Rij', 'age': 199},
    ]
    return render(request,"index.html", context = {
        'peoples' : people
    })

def new(request):
    return HttpResponse("New Server")

def success_page(request):
    return HttpResponse("<h1> This is success page </h1>")

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')