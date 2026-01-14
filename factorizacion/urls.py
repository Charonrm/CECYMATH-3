from django.urls import path
from . import views

urlpatterns = [
    path('', views.factorizacion_view, name='factorizacion'),
]
