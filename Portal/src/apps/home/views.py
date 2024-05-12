from django.shortcuts import render
from django.views.generic import TemplateView
from apps.issue_management.models import (
    Issue
)

def main(request):
    issues = Issue.objects.all()
    context = {"issues":issues}
    return render(request, "home/main.html", context=context)