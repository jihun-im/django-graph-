from django.shortcuts import render
from django.http import HttpResponse

def pageName(request):
    return HttpResponse("Hello, world. You're at the polls index.2")
