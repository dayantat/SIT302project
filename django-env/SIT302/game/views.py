from django.shortcuts import render
from django.views import generic
# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello this is the game view")
