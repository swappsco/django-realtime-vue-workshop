# myapp/views.py
from django.shortcuts import render


def index(request):
    return render(request, "surveys/index.html", {})


def room(request, room_name):
    return render(request, "surveys/detail.html", {"room_name": room_name})

