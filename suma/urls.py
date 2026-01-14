from django.urls import path
from . import views

urlpatterns = [
    path('', views.suma_view, name='suma'),
]
