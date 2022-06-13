"""banking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework import routers

from core import views

router = routers.SimpleRouter()

router.register(r'categories', views.CategoryModelViewSet, basename="category") #do not need forward slash as it will automatically add for us
router.register(r'transactions', views.TransactionModelViewSet, basename="transaction")


urlpatterns = [
    path('currencies/', views.CurrencyList.as_view(), name="currencies"),
] + router.urls
