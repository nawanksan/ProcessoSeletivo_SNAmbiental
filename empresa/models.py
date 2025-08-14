from django.db import models
from endereco.models import Endereco
from django.core.validators import MinLengthValidator, RegexValidator

class Empresa(models.Model):
    id = models.AutoField(primary_key=True)
    vNome_fantasia = models.CharField(max_length=80)
    vNome_razao_social = models.CharField(max_length=80)
    vCnpj = models.CharField(
    max_length=14,
    
    unique=True,
    validators=[
        MinLengthValidator(14, message="O CNPJ deve ter 14 dígitos"),
    ]
)
    vEmail = models.CharField(max_length=40)
    vObservacao = models.CharField(max_length=200, blank=True, null=True)
    iCod_endereco = models.OneToOneField(
        Endereco,
        on_delete=models.CASCADE, unique=True
    )
    
    def __str__(self):
        return f'{self.vNome_fantasia} ({self.vCnpj})'