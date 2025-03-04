from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Gasto
from .serializers import GastoSerializer

# Create your views here.


class GastoViewSet(viewsets.ModelViewSet):
    queryset = Gasto.objects.all()
    serializer_class = GastoSerializer
    permission_classes = [IsAuthenticated]
