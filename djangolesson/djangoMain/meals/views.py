from django.shortcuts import render
from .models import Articles

def meals(request):
    meals = Articles.objects.all()
    return render(request, "mainView/firstShablon2.html", {'meals': meals})