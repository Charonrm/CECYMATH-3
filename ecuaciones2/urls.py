from django.urls import path
from . import views

urlpatterns = [
    path('', views.ecuacion2_view, name='ecuaciones2'),
]
