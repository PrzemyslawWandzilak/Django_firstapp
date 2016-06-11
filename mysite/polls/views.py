from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Cześć Kochanie. Hi, hi")

# Create your views here.
