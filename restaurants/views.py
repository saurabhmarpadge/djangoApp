import random
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def home(request):
    num = [
        random.randint(0, 100),
        random.randint(0, 100),
        random.randint(0, 100),
        ]
    content = {
        "html_var": "Dragon Ball",
        "num":num
        }
    return render(request, "home.html", content)

def about(request):
    num = [
        random.randint(0,100),
        random.randint(0, 100),
        random.randint(0, 100),
        ]
    content = {
        "html_var": "Dragon Ball",
        "num":num
        }
    return render(request, "about.html", content)

def contact(request):
    num = [
        random.randint(0,100),
        random.randint(0, 100),
        random.randint(0, 100),
        ]
    content = {
        "html_var": "Dragon Ball",
        "num": num
        }
    return render(request, "contact.html", content)