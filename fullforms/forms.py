from django.forms import ModelForm
from .models import FullForms


class FullformForm(ModelForm):
    class Meta:
        model = FullForms
        fields = ('shortForm', 'fullForm')
