"""
URL configuration for djangoMain project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add djangoMain URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add djangoMain URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add djangoMain URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainView.urls'), name="home"),
    path('drinks/', include('drink.urls'), name="drinks"),
    path('meals/', include('meals.urls'), name="meals"),
    path('deserts/', include('deserts.urls'), name="deserts"),
    path('news/', include('news.urls'), name="news"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
