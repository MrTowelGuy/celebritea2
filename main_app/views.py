from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from main_app.models import Tea, Celeb
from main_app.forms import SightingForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


# Add new view
def teas_index(request):
    teas = Tea.objects.all()
    return render(request, 'teas/index.html', { 'teas': teas})

def teas_detail(request, tea_id):
  tea = Tea.objects.get(id=tea_id)
  sighting_form = SightingForm()
  return render(request, 'teas/detail.html', {
     'tea': tea, 'sighting_form':sighting_form })


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

def celebs_index(request):
    celebs = Celeb.objects.all()
    return render(request, 'celebs/index.html', {'celebs': celebs})

def celebs_detail(request, celeb_id):
  celeb = Celeb.objects.get(id=celeb_id)
  return render(request, 'celebs/detail.html', { 'celeb': celeb })

class CelebCreate(CreateView):
  model = Celeb
  fields = ['name', 'description']
  success_url = '/celebs/'


class CelebUpdate(UpdateView):
  model = Celeb
  fields = ['name','description']

class CelebDelete(DeleteView):
  model = Celeb
  success_url = '/celebs/'