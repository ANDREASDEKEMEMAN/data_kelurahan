from rest_framework import serializers
from .models import Warga, Pengaduan

class WargaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warga
        fields = ['id', 'nik', 'nama_lengkap', 'alamat', 'no_telepon']
class WargaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warga
        fields = '__all__'

# --- Serializer Baru untuk Modul 7 ---
class PengaduanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pengaduan
        fields = '__all__'