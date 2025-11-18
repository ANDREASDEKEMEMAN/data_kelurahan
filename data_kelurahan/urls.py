# data_kelurahan/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),

    # URL untuk halaman web (HTML biasa)
    path('warga/', include('warga.urls')),

    # 🔹 URL untuk API (DRF)
    path('api/', include('warga.api_urls')),

    # 🔹 LOGIN untuk DRF Browsable API → supaya tombol LOGIN muncul
    path('api-auth/', include('rest_framework.urls')),

    # 🔹 Redirect ke halaman utama aplikasi
    path('', RedirectView.as_view(url='/warga/')),

    # 🔹 Token login API
    path('api/auth/token/', obtain_auth_token, name='api-token-auth'),
    path('api/', include('warga.api_urls')),

]


