from django.urls import path
from . import views

urlpatterns = [
    path('', views.multiplicacion_view, name='multiplicacion'),
]
