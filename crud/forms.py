from django.forms import ModelForm
from .models import CepModel

class cepForm(ModelForm):
    class Meta:
        fields = ['cep']
        model = CepModel