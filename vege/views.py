from django.shortcuts import render
from vege.models import Receipe

def receipes(request):
    
    if request.method == "POST":
        data = request.POST
        name = data.get("name")
        desc = data.get("description")

        Receipe.objects.create(name = name, description = desc)
    print(request.method)
    print(request.POST)
    return render(request, 'receipes.html')