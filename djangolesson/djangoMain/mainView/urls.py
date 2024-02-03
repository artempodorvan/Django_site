from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('buying', views.buying, name="buying"),
    path('drinks', views.drink, name="drinks"),
    path('meals', views.index2, name="meals"),
    path('deserts', views.index3, name="deserts"),
    path('about', views.about, name="about"),
    path('contacts', views.settings, name="contacts")
]
