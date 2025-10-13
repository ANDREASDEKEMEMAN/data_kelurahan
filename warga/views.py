from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Warga, Pengaduan

# ======== WARGA ========
class WargaListView(ListView):
    model = Warga
    template_name = 'warga/warga_list.html'
    context_object_name = 'warga_list'

class WargaCreateView(CreateView):
    model = Warga
    template_name = 'warga/warga_form.html'
    fields = ['nik', 'nama_lengkap', 'alamat', 'no_telepon']
    success_url = reverse_lazy('warga_list')

class WargaDetailView(DetailView):
    model = Warga
    template_name = 'warga/warga_detail.html'
    context_object_name = 'warga'

# ======== PENGADUAN ========
class PengaduanListView(ListView):
    model = Pengaduan
    template_name = 'warga/pengaduan_list.html'
    context_object_name = 'pengaduan_list'
