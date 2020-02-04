# chat/urls.py
from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("<str:room_name>/", views.room, name="detail"),
]
