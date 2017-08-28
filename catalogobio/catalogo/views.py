from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from .models import Species
from .forms import SpeciesForm

# Create your views here.

def index(request):
    species_list = Species.objects.all()
    context = {'species_list': species_list}
    return render(request, 'catalogo/index.html', context)

def species_view(request):
    if request.method != 'GET':
        return HttpResponseRedirect(reverse('images:index'))

    id = request.GET.get('id')
    if not id:
        return HttpResponseRedirect(reverse('images:index'))

    species = Species.objects.get(id=id)
    context = {'species': species}
    return render(request, 'catalogo/species_view.html', context)

def species_create(request):
    if request.method == 'POST':
        form = SpeciesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('images:index'))
    else:
        form = SpeciesForm()

    return render(request, 'catalogo/species_create.html', {'form': form})

def login_view(request):

    if request.user.is_authenticated():
        return redirect(reverse('catalogo/index.html'))

    message = ""

    if(request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(reverse('catalogo/index.html'))
        else:
            message = "Nombre de usuario o clave incorrecta"

    return render(request, 'catalogo/login.html', {'message':message})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("catalogo/index.html"))



