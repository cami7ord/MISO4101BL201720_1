from django.conf.urls import url
from . import views

app_name = 'catalogo'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^species_create/$',views.species_create, name='addspecies'),
    url(r'^species_view/$',views.species_view, name='viewspecies'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
]
