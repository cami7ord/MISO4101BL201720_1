from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^species_create/$',views.species_create, name='addspecies'),
    url(r'^species_view/$',views.species_view, name='viewspecies'),
]
