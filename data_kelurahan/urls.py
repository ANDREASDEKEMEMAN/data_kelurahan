# data_kelurahan/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('warga/', include('warga.urls')),
    # 🔹 Tambahkan redirect otomatis agar '/' langsung ke daftar warga
    path('', RedirectView.as_view(url='/warga/')),
]

