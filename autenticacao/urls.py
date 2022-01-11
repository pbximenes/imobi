
from django.contrib import admin
from django.urls import path, include
from autenticacao import urls

urlpatterns = [
    path('auth/', admin.site.urls)
]
