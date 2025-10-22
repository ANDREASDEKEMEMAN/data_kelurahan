# warga/urls.py
from django.urls import path
from .views import (
    # View untuk Warga
    WargaListView, WargaDetailView, WargaCreateView,
    WargaUpdateView, WargaDeleteView,
    # View untuk Pengaduan
    PengaduanListView, PengaduanCreateView,
    PengaduanUpdateView, PengaduanDeleteView
)

urlpatterns = [
    # ======== WARGA ========
    path('', WargaListView.as_view(), name='warga-list'),
    path('tambah/', WargaCreateView.as_view(), name='warga-tambah'),
    path('<int:pk>/', WargaDetailView.as_view(), name='warga-detail'),
    path('<int:pk>/edit/', WargaUpdateView.as_view(), name='warga-edit'),    # ✅ URL untuk edit warga
    path('<int:pk>/hapus/', WargaDeleteView.as_view(), name='warga-hapus'),  # ✅ URL untuk hapus warga

    # ======== PENGADUAN ========
    path('pengaduan/', PengaduanListView.as_view(), name='pengaduan-list'),
    path('pengaduan/tambah/', PengaduanCreateView.as_view(), name='pengaduan-tambah'),
    path('pengaduan/<int:pk>/edit/', PengaduanUpdateView.as_view(), name='pengaduan-edit'),  # ✅ URL untuk edit pengaduan
    path('pengaduan/<int:pk>/hapus/', PengaduanDeleteView.as_view(), name='pengaduan-hapus'), # ✅ URL untuk hapus pengaduan
]


