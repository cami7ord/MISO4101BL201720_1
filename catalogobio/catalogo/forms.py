from .models import Species,User, UserProfile
from django.forms import ModelForm

class SpeciesForm(ModelForm):

    class Meta:
        model = Species
        fields = [
            'name',
            'scientific_name',
            'category',
            'picture',
            'description',
            ]
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            ]

#class ProfileForm(ModelForm):
    #class Meta:
     #   model = UserProfile
      #  fields = [
       #     'country',
        #    'city',
         #   'interests',
        #]
