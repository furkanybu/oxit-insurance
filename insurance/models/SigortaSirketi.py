from django.db import models


class SigortaSirketi(models.Model):
    sirket_adi = models.CharField(max_length=250, verbose_name='Şirket Adı')
    aktif = models.BooleanField(verbose_name='Etkin', null=True, blank=True)

    creationDate = models.DateTimeField(auto_now_add=True, verbose_name='Kayıt Tarihi')
    modificationDate = models.DateTimeField(auto_now=True, verbose_name='Güncelleme Tarihi')
