from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('teas/', views.teas_index, name='index'),
  path('teas/<int:tea_id>/', views.teas_detail, name='detail'),
  path('teas/create/', views.TeaCreate.as_view(), name='teas_create'),
  path('teas/<int:pk>/update/', views.TeaUpdate.as_view(), name='teas_update'),
  path('teas/<int:pk>/delete/', views.TeaDelete.as_view(), name='teas_delete'),
  path('celebs/', views.celebs_index, name='index'),
  path('celebs/<int:celeb_id>/', views.celebs_detail, name='detail'),
  path('celebs/create/', views.CelebCreate.as_view(), name='celebs_create'),
  path('celebs/<int:pk>/update/', views.CelebUpdate.as_view(), name='celebs_update'),
  path('celebs/<int:pk>/delete/', views.CelebDelete.as_view(), name='celebs_delete'),
  path('teas/<int:tea_id>/add_sighting/', views.add_sighting, name='add_sighting'),
]
