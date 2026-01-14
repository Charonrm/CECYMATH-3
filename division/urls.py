from django.urls import path
from . import views

urlpatterns = [
    path('', views.division_view, name='division'),
]
