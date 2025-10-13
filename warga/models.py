from django.db import models

class Warga(models.Model):
    nik = models.CharField(max_length=16, unique=True, verbose_name="Nomor Induk Kependudukan")
    nama_lengkap = models.CharField(max_length=100, verbose_name="Nama Lengkap")
    alamat = models.TextField(verbose_name="Alamat Tinggal")
    no_telepon = models.CharField(max_length=15, blank=True, verbose_name="Nomor Telepon")
    tanggal_registrasi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nama_lengkap


class Pengaduan(models.Model):
    pelapor = models.ForeignKey(Warga, on_delete=models.CASCADE, related_name='pengaduan')
    judul = models.CharField(max_length=200)
    deskripsi = models.TextField()
    status = models.CharField(max_length=20, choices=[
        ('baru', 'Baru'),
        ('proses', 'Sedang Diproses'),
        ('selesai', 'Selesai')
    ], default='baru')

    def __str__(self):
        return f"{self.judul} - {self.pelapor.nama_lengkap}"

