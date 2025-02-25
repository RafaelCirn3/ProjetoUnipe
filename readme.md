Videos recomendados:

Aprenda Git e Github em 5 minutos
https://www.youtube.com/watch?v=-l4Aa8wef8s

Funções e Classes em Python 
https://www.youtube.com/watch?v=-VdD-O6lL7w

Aprenda Python na Prática (Listas, Tuplas, Dicionários) 
https://www.youtube.com/watch?v=0zYuLLIzPIQ

Estrutura Básica de um Projeto em Django
https://www.youtube.com/watch?v=4u0aI-90KnU&t=126s

Learn Docker in 7 Easy Steps - Full Beginner's Tutorial
https://www.youtube.com/watch?v=gAkwW2tuIqE&t=160s


# Documentação para o projeto Django "ConsultaCEP"

## 1. Configuração Inicial do Projeto

### Criar e ativar um ambiente virtual:
```sh
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### Instalar o Django:
```sh
pip install django
```

### Criar o projeto Django:
```sh
django-admin startproject ConsultaCEP
cd ConsultaCEP
```

### Criar o aplicativo "enderecos":
```sh
python manage.py startapp enderecos
```

### Registrar o app `enderecos` no `settings.py`:
No arquivo `ConsultaCEP/settings.py`, adicione:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'enderecos',
]
```

## 2. Criar o Modelo
No arquivo `enderecos/models.py`, defina o modelo:
```python
from django.db import models

class EnderecosModel(models.Model):
    cep = models.CharField(max_length=9)
    bairro = models.CharField(max_length=100)
    localidade = models.CharField(max_length=100)
    regiao = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.cep} - {self.localidade}"
```

### Criar e aplicar as migrações:
```sh
python manage.py makemigrations enderecos
python manage.py migrate
```

## 3. Criar os Forms
No arquivo `enderecos/forms.py`, defina o form:
```python
from django import forms
from .models import EnderecosModel

class EnderecoForm(forms.ModelForm):
    class Meta:
        model = EnderecosModel
        fields = ['cep']
```

## 4. Criar as Views
No arquivo `enderecos/views.py`, defina as views:
```python
from django.views.generic import FormView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import EnderecosModel
from .forms import EnderecoForm

class EnderecoCreateView(FormView):
    template_name = 'enderecos/form.html'
    form_class = EnderecoForm
    success_url = reverse_lazy('endereco_list')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class EnderecoListView(ListView):
    model = EnderecosModel
    template_name = 'enderecos/list.html'
    context_object_name = 'enderecos'

class EnderecoUpdateView(UpdateView):
    model = EnderecosModel
    fields = ['cep', 'bairro', 'localidade', 'regiao']
    template_name = 'enderecos/form.html'
    success_url = reverse_lazy('endereco_list')

class EnderecoDeleteView(DeleteView):
    model = EnderecosModel
    template_name = 'enderecos/confirm_delete.html'
    success_url = reverse_lazy('endereco_list')
```

## 5. Configurar as URLs
No arquivo `enderecos/urls.py`, defina as rotas:
```python
from django.urls import path
from .views import EnderecoCreateView, EnderecoListView, EnderecoUpdateView, EnderecoDeleteView

urlpatterns = [
    path('', EnderecoListView.as_view(), name='endereco_list'),
    path('novo/', EnderecoCreateView.as_view(), name='endereco_create'),
    path('<int:pk>/editar/', EnderecoUpdateView.as_view(), name='endereco_update'),
    path('<int:pk>/deletar/', EnderecoDeleteView.as_view(), name='endereco_delete'),
]
```

No arquivo `ConsultaCEP/urls.py`, inclua as rotas do app:
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('enderecos/', include('enderecos.urls')),
]
```

## 6. Criar os Templates
Crie um diretório `templates/enderecos/` dentro do app e adicione os arquivos:

**`form.html`**:
```html
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Salvar</button>
</form>
```

**`list.html`**:
```html
<ul>
    {% for endereco in enderecos %}
        <li>{{ endereco.cep }} - {{ endereco.localidade }}
            <a href="{{ endereco.pk }}/editar/">Editar</a>
            <a href="{{ endereco.pk }}/deletar/">Deletar</a>
        </li>
    {% endfor %}
</ul>
<a href="novo/">Adicionar Novo</a>
```

**`confirm_delete.html`**:
```html
<form method="post">
    {% csrf_token %}
    <p>Tem certeza que deseja deletar este endereço?</p>
    <button type="submit">Confirmar</button>
</form>
```

## 7. Rodar o Servidor
```sh
python manage.py runserver
```

Agora você pode acessar `http://127.0.0.1:8000/enderecos/` para visualizar e gerenciar os endereços.

