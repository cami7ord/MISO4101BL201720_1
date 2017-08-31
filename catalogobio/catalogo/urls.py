from django.conf.urls import url
from . import views

app_name = 'catalogo'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^species_create/$',views.species_create, name='addspecies'),
    url(r'^species_view/$',views.species_view, name='viewspecies'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^species_update/$',views.speciesUpdate, name='updateSpecies'),
    url(r'^user_update/$',views.userUpdate, name='userUpdate'),
    url(r'^user_update_action/$',views.updateInformation, name='userUpdateAction'),
    url(r'^signup/$',views.signup, name='signup'),
    url(r'^comment/$',views.addComment, name='comment'),
]
