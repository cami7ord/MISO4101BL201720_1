from .models import Species, User, Comment
from django.forms import ModelForm, TextInput


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


class CommentForm(ModelForm):
    READONLY_FIELDS = ('email')

    class Meta:
        model = Comment
        fields = [
            'email',
            'text',
        ]

