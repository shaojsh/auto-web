

from django.http import JsonResponse, HttpRequest
from django.shortcuts import render



def index(request: HttpRequest):
    return render(request, 'index.html')
