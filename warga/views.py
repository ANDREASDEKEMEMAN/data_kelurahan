# warga/views.py
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Warga, Pengaduan
from .forms import WargaForm, PengaduanForm

# ======================================================
#                 VIEW UNTUK HTML (TIDAK DIUBAH)
# ======================================================

# ----------- WARGA (HTML) -----------
class WargaListView(ListView):
    model = Warga
    template_name = 'warga/warga_list.html'
    context_object_name = 'warga_list'

class WargaDetailView(DetailView):
    model = Warga
    template_name = 'warga/warga_detail.html'
    context_object_name = 'warga'

class WargaCreateView(CreateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html'
    success_url = reverse_lazy('warga-list')

class WargaUpdateView(UpdateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html'
    success_url = reverse_lazy('warga-list')

class WargaDeleteView(DeleteView):
    model = Warga
    template_name = 'warga/warga_confirm_delete.html'
    success_url = reverse_lazy('warga-list')


# ----------- PENGADUAN (HTML) -----------
class PengaduanListView(ListView):
    model = Pengaduan
    template_name = 'warga/pengaduan_list.html'
    context_object_name = 'pengaduan_list'

class PengaduanCreateView(CreateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html'
    success_url = reverse_lazy('pengaduan-list')

class PengaduanUpdateView(UpdateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html'
    success_url = reverse_lazy('pengaduan-list')

class PengaduanDeleteView(DeleteView):
    model = Pengaduan
    template_name = 'warga/pengaduan_confirm_delete.html'
    success_url = reverse_lazy('pengaduan-list')
# ======================================================
#                       API MODUL 7
# ======================================================
from rest_framework import viewsets, filters   # ← WAJIB ADA
from .serializers import WargaSerializer, PengaduanSerializer

# --- API CRUD Warga (ModelViewSet) ---
class WargaViewSet(viewsets.ModelViewSet):
    queryset = Warga.objects.all().order_by('-id')
    serializer_class = WargaSerializer

# --- API CRUD Pengaduan (ModelViewSet) ---
class PengaduanViewSet(viewsets.ModelViewSet):
    queryset = Pengaduan.objects.all().order_by('-id')
    serializer_class = PengaduanSerializer

    # Search
    filter_backends = [filters.SearchFilter]
    search_fields = ['judul', 'isi_laporan', 'lokasi']
