from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="profiles", null=True, blank=True)
    nama = models.CharField(max_length=100)
    namaPerusahaan = models.CharField(max_length=100)
    emailPerusahaan = models.EmailField()
    nomorTelepon = models.CharField(max_length=15)

    def __str__(self):
        return self.nama