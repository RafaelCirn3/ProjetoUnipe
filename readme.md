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


# Documentação para criar um projeto Django

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
django-admin startproject projeto
cd projeto
```

### Criar o aplicativo "app":
```sh
python manage.py startapp app
```

### Registrar o app `app` no `settings.py`:
No arquivo `projeto/settings.py`, adicione:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
]
```

## 2. Criar o Modelo
No arquivo `app/models.py`, defina o modelo:
```python
from django.db import models

class ExemploModel(models.Model):

```

### Criar e aplicar as migrações:
```sh
python manage.py makemigrations 
python manage.py migrate
```

## 3. Criar os Forms
No arquivo `app/forms.py`, defina o form;


## 4. Criar as Views
No arquivo `app/views.py`, defina as views;

## 5. Configurar as URLs
No arquivo `App/urls.py`, defina as rotas;

No arquivo `Project/urls.py`, inclua as rotas do app;


## 6. Criar os Templates
Crie um diretório `templates/App/` dentro do app e adicione os arquivos:

**`form.html`**:
**`list.html`**:
**`confirm_delete.html`**:

## 7. Rodar o Servidor
```sh
python manage.py runserver
```

Agora você pode acessar `http://127.0.0.1:8000/api/` para visualizar e gerenciar os endereços.

