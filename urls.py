from django.conf.urls import url, include
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^SpringLoaded/', views.SpringLoaded, name = "SpringLoaded"),
    url(r'^Envelope/', views.Envelope, name = "Envelope"),
    url(r'^', views.index, name = "index"),
]
