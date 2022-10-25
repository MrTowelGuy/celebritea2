from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟﾉ</h1>')

def about(request):
    return HttpResponse('<h1>Spill the tea</h1>')