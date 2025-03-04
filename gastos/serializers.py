from rest_framework import serializers
from .models import Gasto


class GastoSerializer(serializers.ModelSerializer):
    monto = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        coerce_to_string=False)

    class Meta:
        model = Gasto
        fields = '__all__'
