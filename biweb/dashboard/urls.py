from django.urls import path
from . import views


urlpatterns = [
    path("", views.index),
    path("charts", views.charts),
    path("listVille/<limit>", views.listVille)
]