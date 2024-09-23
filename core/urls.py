from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Define a view padrão para a raiz do núcleo
]