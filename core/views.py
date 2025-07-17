from django.shortcuts import render
from .models import Profile

def home(request):
    profile = Profile.objects.first()
    return render(request, 'home.html', {'profile': profile})

def trade_here(request):
    return render(request, 'trade_here.html')
