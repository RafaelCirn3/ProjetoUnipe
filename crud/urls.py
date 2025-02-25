from django.urls import path
from .views import CepListView, CepCreateView, CepUpdateView, CepDeleteView

urlpatterns = [
    path('criar/', CepCreateView.as_view(), name= 'cria_cep'),
    path('lista/', CepListView.as_view(), name='lista_cep'),
    path('atualiza/<int:pk>', CepUpdateView.as_view(), name='atualiza_cep'),
    path('deleta/<int:pk>', CepDeleteView.as_view(), name='deleta_cep')
]
