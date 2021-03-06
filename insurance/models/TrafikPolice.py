from django.db import models

from insurance.models import Teklif


class TrafikPolice(models.Model):
    teklif = models.ForeignKey(Teklif, on_delete=models.CASCADE)
    police_file = models.FileField(upload_to='uploads/%Y/%m/%d/')
    police_numarasi = models.CharField(max_length=128, null=True, blank=True, default="")
    creationDate = models.DateTimeField(auto_now_add=True, verbose_name='Kayıt Tarihi')
    modificationDate = models.DateTimeField(auto_now=True, verbose_name='Güncelleme Tarihi')
