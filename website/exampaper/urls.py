
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='home'),
    path('SEM.html', views.semester,name='semester'),
]
