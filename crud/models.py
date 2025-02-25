from django.db import models

class CepModel(models.Model):
    cep = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    def __str__(self):
        return f'{self.cep} - {self.cidade}'
# Create your models here.
