from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Tea

def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟﾉ</h1>')

def about(request):
    return render(request, 'about.html')


# Add new view
def teas_index(request):
    teas = Tea.objects.all()
    return render(request, 'teas/index.html', { 'teas': teas})

def teas_detail(request, tea_id):
  tea = Tea.objects.get(id=tea_id)
  return render(request, 'teas/detail.html', { 'tea': tea })


class TeaCreate(CreateView):
  model = Tea
  fields = ['title', 'type', 'description', 'witnesses']
  success_url = '/teas/'


class TeaUpdate(UpdateView):
  model = Tea
  fields = ['title', 'description', 'witnesses']

class TeaDelete(DeleteView):
  model = Tea
  success_url = '/teas/'
