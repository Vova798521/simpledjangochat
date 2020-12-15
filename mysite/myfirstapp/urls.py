
from django.urls import path
from . import views


urlpatterns = [
    path('vova', views.index),
    path('voval', views.lesyuck),
]
