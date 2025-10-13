from django.urls import path
from .views import WargaListView, WargaDetailView, WargaCreateView, PengaduanListView

urlpatterns = [
    path('', WargaListView.as_view(), name='warga_list'),
    path('<int:pk>/', WargaDetailView.as_view(), name='warga_detail'),
    path('tambah/', WargaCreateView.as_view(), name='warga_tambah'),
    path('pengaduan/', PengaduanListView.as_view(), name='pengaduan_list'),
]
