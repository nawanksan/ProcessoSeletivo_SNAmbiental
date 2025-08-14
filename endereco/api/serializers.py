from rest_framework import serializers
from endereco.models import Endereco

class EnderecoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'