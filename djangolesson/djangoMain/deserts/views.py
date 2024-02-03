from django.shortcuts import render
from .models import Articles

def deserts(request):
    deserts = Articles.objects.all()
    return render(request, "mainView/firstShablon3.html", {'deserts': deserts})
