from django.urls import path

from django101.cities.views import index

urlpatterns = [
    path('', index),
]
