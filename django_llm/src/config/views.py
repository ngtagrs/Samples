from django import views
from django.shortcuts import render

def index(request):
    return render(request, "index.html")

