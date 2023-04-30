from django.urls import path

from . import views

urlpatterns = [
    path('firstApp', views.first_app, name='first_app'),
]
