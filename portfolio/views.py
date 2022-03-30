from django.shortcuts import render

from portfolio.models import project

def home(request):
    projects= project.objects.all()
    return render(request, 'portfolio/home.html', {'projects':projects})
