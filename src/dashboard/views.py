# dashboard/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'dashboard/index.html', {})

def room(request):
    return render(request, 'dashboard/room.html')
