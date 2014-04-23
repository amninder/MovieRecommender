from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from movie_names.models import *

def index(request):
    return render(request, "index.html")