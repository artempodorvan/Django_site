from django.shortcuts import render
from .models import Articles

def drink(request):
    drinks = Articles.objects.all()
    return render(request, "mainView/firstShablon1.html", {'drinks': drinks})
