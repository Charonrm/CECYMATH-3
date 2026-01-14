from django.urls import path
from . import views

urlpatterns = [
    path('', views.polinomios_view, name='polinomios'),
]
