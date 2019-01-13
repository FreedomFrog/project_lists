from django.shortcuts import render
from django.views.generic import ListView
from . models import Winery

# Create your views here.
class WineryList(ListView):
    model = Winery
    context_object_name = 'wineries'