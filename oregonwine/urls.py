from django.urls import path
from . import views

urlpatterns = [
    path('', views.WineryList.as_view(), name='WineryList'),
]