from .models import Species
from django.forms import ModelForm

class SpeciesForm(ModelForm):

    class Meta:
        model = Species
        fields = [
            'name',
            'scientific_name',
            'category',
            'picture',
            'description'
            ]
