from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from main_app.models import Tea, Celeb
from main_app.forms import SightingForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def assoc_celeb(request, tea_id, celeb_id):
  # Note that you can pass a toy's id instead of the whole object
  Tea.objects.get(id=tea_id).celebs.add(celeb_id)
  return redirect('detail', tea_id=tea_id)


def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

@login_required
def teas_index(request):
    teas = Tea.objects.filter(user=request.user)
    return render(request, 'teas/index.html', { 'teas': teas})

@login_required
def teas_detail(request, tea_id):
    tea = Tea.objects.get(id=tea_id)
    celebs_tea_doesnt_have = Celeb.objects.exclude(id__in = tea.celebs.all().values_list('id'))
    sighting_form = SightingForm()
    return render(request, 'teas/detail.html', {
        'tea': tea, 'sighting_form':sighting_form, 
        'celebs': celebs_tea_doesnt_have
        })

@login_required
def add_sighting(request, tea_id):
    form = SightingForm(request.POST)
    if form.is_valid():
        new_sighting = form.save(commit=False)
        new_sighting.tea_id = tea_id
        new_sighting.save()
    return redirect('detail', tea_id=tea_id)


class TeaCreate(LoginRequiredMixin, CreateView):
  model = Tea
  fields = ['title', 'type', 'description', 'witnesses']
  def form_valid(self,form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class TeaUpdate(LoginRequiredMixin, UpdateView):
  model = Tea
  fields = ['title', 'description', 'witnesses']

class TeaDelete(LoginRequiredMixin, DeleteView):
  model = Tea
  success_url = '/teas/'

@login_required
def celebs_index(request):
    celebs = Celeb.objects.all()
    return render(request, 'celebs/index.html', {'celebs': celebs})

@login_required
def celebs_detail(request, celeb_id):
  celeb = Celeb.objects.get(id=celeb_id)
  return render(request, 'celebs/detail.html', { 'celeb': celeb })

class CelebCreate(LoginRequiredMixin, CreateView):
  model = Celeb
  fields = ['name', 'description']
  success_url = '/celebs/'


class CelebUpdate(LoginRequiredMixin, UpdateView):
  model = Celeb
  fields = ['name','description']

class CelebDelete(LoginRequiredMixin, DeleteView):
  model = Celeb
  success_url = '/celebs/'