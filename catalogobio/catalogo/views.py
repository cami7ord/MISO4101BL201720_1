import json

from django.contrib.auth import authenticate, login, logout
from django.core import serializers
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from catalogobio import settings
from .models import Category
from .models import Species
from .models import Category
from .models import User
from .models import UserProfile
from .models import Comment
from .forms import SpeciesForm, UserForm, CommentForm

# Create your views here.


def index(request):
    category = request.GET.get('category')

    if request.user.is_authenticated():
        if category:
            species_list = Species.objects.filter(category=category)
        else:
            species_list = Species.objects.all()
        category_list = Category.objects.all()
        context = {
            'species_list': species_list,
            'category_list': category_list,
            'category': category,
        }
        return render(request, 'catalogo/index.html', context)
    else:
        return HttpResponseRedirect(reverse('catalogo:login'))


def species_list(request):
    category = request.GET.get('category')
    # import IPython; IPython.embed()
    if category:
        species_list = Species.objects.filter(category=category)
    else:
        species_list = Species.objects.all()
    category_list = Category.objects.all()
    context = {
        'species_list': species_list,
        'category_list': category_list,
        'category': category,
    }
    return render(request, 'catalogo/index_list.html', context)


def species_view(request):
    if request.method != 'GET':
        return HttpResponseRedirect(reverse('images:index'))

    id = request.GET.get('id')
    if not id:
        return HttpResponseRedirect(reverse('images:index'))

    species = Species.objects.get(id=id)
    categories = Category.objects.all()
    comments = Comment.objects.filter(species_id=id)
    context = {'species': species, 'categories': categories, 'comments': comments}
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
        return redirect(reverse('catalogo:index'))

    message = ""

    if(request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(reverse('catalogo:index'))
        else:
            message = "Nombre de usuario o clave incorrecta"

    return render(request, 'catalogo/login.html', {'message': message})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("catalogo:index"))


def speciesUpdate(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        s_name = request.POST.get('s_name')
        category = Category.objects.get(name=request.POST.get('category'))
        description = request.POST.get('description')

        Species.objects.filter(id=request.POST.get('id')).update(name=name, scientific_name=s_name, category=category,
                                                                 description=description)

        return HttpResponse(True)

    else:
        return HttpResponse(False)


def userUpdate(request):
    if request.method == 'GET':
        if request.user.is_authenticated():
            current_user = User.objects.get(id=request.user.id)
            context = {'user': current_user}
            return render(request, 'catalogo/user_view.html', context)

        else:
            return HttpResponseRedirect(reverse('catalogo:login'))


def updateInformation(request):

    if request.method == 'GET':
        name = request.GET.get('name')
        last_name = request.GET.get('lname')
        username = request.GET.get('uname')

        country = request.GET.get('country')
        city = request.GET.get('city')
        interests = request.GET.get('interests')

        User.objects.filter(id=request.user.id).update(
            first_name=name, last_name=last_name, username=username)
        UserProfile.objects.filter(user_id=request.user.id).update(
            country=country, city=city, interests=interests)

        return HttpResponseRedirect(reverse('catalogo:index'))

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        jsonUser = json.loads(request.body)

        username = jsonUser['username']
        first_name = jsonUser['first_name']
        last_name = jsonUser['last_name']
        email = jsonUser['email']
        password = jsonUser['password']

        user_model = User.objects.create_user(username=username, password=password)
        user_model.first_name = first_name
        user_model.last_name = last_name
        user_model.email = email
        user_model.save()

        last_user = User.objects.last()

        user_profile = UserProfile()
        user_profile.city = jsonUser['city']
        user_profile.country = jsonUser['country']
        user_profile.interests = jsonUser['interest']
        user_profile.user_id = last_user.id

        user_profile.save()

        subject = "Bienvenida"
        message = "Hola!/n Bienvenida monitora, Gracias por probar nuestra aplicacion"
        from_email = settings.EMAIL_HOST_USER
        to_list = [email, settings.EMAIL_HOST_USER]

        send_mail(subject, message, from_email, to_list, fail_silently=True)

        return HttpResponse(serializers.serialize("json", [user_model, user_profile]))

    else:

        form = UserForm()
        return render(request, 'catalogo/signup.html', {'form': form})  # , 'profileform':profileform})


def addComment(request):
    if request.user.is_authenticated():

        form = CommentForm(request.POST)
        if request.method == 'GET':

            return render(request, 'catalogo/comment.html', {'form': form, 'id': request.GET.get('species_id')})

        else:
            if form.is_valid():

                comment_model = Comment()
                comment_model.email = request.POST.get('email')
                comment_model.text = request.POST.get('text')
                comment_model.species_id = request.GET.get('species_id')

                comment_model.save()

                response = redirect('catalogo:viewspecies')
                response['Location'] += '?id=' + request.GET.get('species_id')
                return response

            else:

                return render(request, 'catalogo/comment.html', {'form': form})

    else:
        return HttpResponseRedirect(reverse('catalogo:login'))
