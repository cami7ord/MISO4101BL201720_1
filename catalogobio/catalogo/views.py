from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Species
from .models import Category
from .models import User
from .models import UserProfile
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
    categories = Category.objects.all()
    context = {'species': species, 'categories': categories}
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

def speciesUpdate(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        s_name = request.POST.get('s_name')
        category = Category.objects.get(name= request.POST.get('category'))
        description = request.POST.get('description')

        Species.objects.filter(id=request.POST.get('id')).update(name= name, scientific_name= s_name, category= category, description= description)

        return HttpResponse(True)

    else:
        return HttpResponse(False)

def userUpdate(request):
    if request.method == 'GET':
        if request.user.is_authenticated():
            current_user = User.objects.get(id= request.user.id)
            context = {'user': current_user}
            return render(request, 'catalogo/user_view.html', context)

        else:
            '''Cambiar x la ruta redirect al login'''
            return HttpResponseRedirect(reverse('images:index'))

def updateInformation (request):

    if request.method == 'GET':
        name = request.GET.get('name')
        last_name = request.GET.get('lname')
        username = request.GET.get('uname')

        country = request.GET.get('country')
        city = request.GET.get('city')
        interests = request.GET.get('interests')

        User.objects.filter(id=request.user.id).update(first_name=name, last_name=last_name, username=username)
        UserProfile.objects.filter(user_id=request.user.id).update(country=country, city=city, interests=interests)

        return HttpResponseRedirect(reverse('images:index'))

