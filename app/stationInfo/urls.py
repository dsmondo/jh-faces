
from django.contrib import admin
from django.urls import path, include

from .views import MainPage, TestJson

urlpatterns = [
    path('', MainPage.as_view()),
    path('test/', TestJson.as_view()),
]

