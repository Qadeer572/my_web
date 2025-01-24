from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<h1>Hello My Name is Qadeer Raza</h1>")