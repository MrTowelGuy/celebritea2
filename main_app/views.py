from django.shortcuts import render
from django.http import HttpResponse
from .models import Tea

def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟﾉ</h1>')

def about(request):
    return render(request, 'about.html')


# Add new view
def teas_index(request):
    teas = Tea.objects.all()
    return render(request, 'teas/index.html', { 'teas': teas})

def teas_detail(request, cat_id):
  tea = Tea.objects.get(id=cat_id)
  return render(request, 'teas/detail.html', { 'tea': tea })