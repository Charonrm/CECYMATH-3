from django.urls import path
from . import views

urlpatterns = [
    path('', views.resta_view, name='resta'),
]
