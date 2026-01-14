from django.urls import path
from . import views

urlpatterns = [
    path('', views.jerarquia_view, name='jerarquia'),
]
