from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Warga
from .serializers import WargaSerializer

class WargaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Warga.objects.all()
    serializer_class = WargaSerializer
    permission_classes = [IsAuthenticated]

class WargaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Warga.objects.all()
    serializer_class = WargaSerializer
    permission_classes = [IsAuthenticated]
