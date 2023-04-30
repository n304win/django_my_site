from django.urls import path

from . import views
from dash_apps import first_app

urlpatterns = [
    path('', views.index, name='index'),
]
