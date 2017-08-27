from django.core.urlresolvers import reverse
from django.shortcuts import render
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
