"""
URL configuration for a django_shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import: from my_app import views
    2. Add a URL to urlpatterns: path('', views.home, name='home')
Class-based views
    1. Add an import: from other_app.views import Home
    2. Add a URL to urlpatterns: path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns: path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from shop_app.views import test, main, contacts, client_goods

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop_app.urls')),
    # path('', include('shop.urls')),
    # path('test/', test, name='test'),
    # path('main/', main, name='main'),
    # path('client_goods/', client_goods, name='client_goods'),
    # path('contacts/', contacts, name='contacts'),
]