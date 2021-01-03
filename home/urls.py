from django.urls import path
from . import views
from .dash_apps.finished_apps import simpleexample
urlpatterns = [
    path("", views.home, name='home'),
    path("information/", views.information, name='information'),
    path("data_source/", views.data_source, name='data_source'),
    path("about/", views.about, name='about')
]
