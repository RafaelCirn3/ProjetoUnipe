import requests
from .models import CepModel
from .forms import cepForm
from django.views.generic import ListView, FormView, UpdateView, DeleteView
from django.urls import reverse_lazy

class CepCreateView(FormView):
    template_name = 'form_cep.html'
    form_class = cepForm
    success_url = reverse_lazy('lista_cep')
    
    def form_valid(self, form):
        cep = form.cleaned_data['cep']
        url = f'https://viacep.com.br/ws/{cep}/json/' 
        resposta = requests.get(url)
        if resposta.status_code == 200:
            dados_endereco = resposta.json()
            CepModel.objects.create(  
                cep=cep,
                cidade=dados_endereco.get('localidade')
            )
        else:
            return 'CEP inválido ou não encontrado'
        return super().form_valid(form)
    
    
class CepListView(ListView):
    model = CepModel
    template_name = 'lista_cep.html'

class CepUpdateView(UpdateView):
    model = CepModel
    fields = ['cep', 'cidade']
    template_name = 'form_cep.html'
    success_url = reverse_lazy('lista_cep')

class CepDeleteView(DeleteView):
    model = CepModel
    template_name = 'deleta_cep.html'
    success_url = reverse_lazy('lista_cep')
# Create your views here.
