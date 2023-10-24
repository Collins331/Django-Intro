from django.urls import path

from . import views

urlpatterns = [
    path("", views.home),
    path("units/", views.units),
    path("fees/", views.fees)
]