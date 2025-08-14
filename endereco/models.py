from django.db import models

class Endereco(models.Model):
    id = models.AutoField(primary_key=True)
    vLogradouro = models.CharField(max_length=80)
    vComplemento = models.CharField(max_length=50, blank=True, null=True)
    vBairro = models.CharField(max_length=40)
    vNumero = models.CharField(max_length=10)
    cUF = models.CharField(max_length=2)

    def __str__(self):
        return f'{self.vLogradouro}, {self.vNumero} - {self.vBairro}/{self.cUF}'