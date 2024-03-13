from django import views
from django.shortcuts import render
# class IndexView(views.View):
#     def get(self, request):
#         return render(request, "index.html")

#     def post(self, request):
#         pass

def index(request):
    return render(request, "index.html")

