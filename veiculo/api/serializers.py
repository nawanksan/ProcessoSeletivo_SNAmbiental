from rest_framework import serializers
from veiculo.models import Veiculo

class VeiculoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        fields = '__all__'