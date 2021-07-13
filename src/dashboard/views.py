# dashboard/views.py
from django.shortcuts import render

def room(request):
    return render(request, 'dashboard/room.html')
