from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
import json

def index(request):
    data = [
        "/mainView/img/texas.png /mainView/img/gril_pizza.jpg /mainView/img/paperoni.jpg /mainView/img/diablo.jpg /mainView/img/margarita.jpg"
    ]
    mains = Articles.objects.all()
    return render(request, "mainView/firstShablon.html", {'mains': mains})

def drink(request):
    data = [
        "/mainView/img/texas.png /mainView/img/gril_pizza.jpg /mainView/img/paperoni.jpg /mainView/img/diablo.jpg /mainView/img/margarita.jpg"
    ]
    mains = Articles.objects.all()
    return render(request, "mainView/firstShablon1.html", {'mains': mains})

def index2(request):
    data = [
        "/mainView/img/texas.png /mainView/img/gril_pizza.jpg /mainView/img/paperoni.jpg /mainView/img/diablo.jpg /mainView/img/margarita.jpg"
    ]
    mains = Articles.objects.all()
    return render(request, "mainView/firstShablon2.html", {'mains': mains})

def index3(request):
    data = [
        "/mainView/img/texas.png /mainView/img/gril_pizza.jpg /mainView/img/paperoni.jpg /mainView/img/diablo.jpg /mainView/img/margarita.jpg"
    ]
    mains = Articles.objects.all()
    return render(request, "mainView/firstShablon3.html", {'mains': mains})

def about(request):
    return render(request, "mainView/secondShablon.html")

def buying(request):
    product_details_json = request.session.get('productDetails', '{}')
    product_details = json.loads(product_details_json)

    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if 'order' in request.POST:
            if form.is_valid():
                form.save()
                return redirect('home')
            else:
                error = 'Monkey do u know how to fill it normally'

        elif 'cancel' in request.POST:
            return redirect('home')

    title = request.GET.get('title', '')
    price = request.GET.get('price', '')
    description = request.GET.get('description', '')

    form = ArticlesForm(initial={'title': title, 'price': price, 'description': description})

    data = {
        'form': form,
        'error': error,
        'product_details': product_details
    }

    return render(request, 'mainView/buying.html', data)
def settings(request):
    return render(request, "mainView/thirdShablon.html")
