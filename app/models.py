from django.db import models

class Maps(models.Model):
    kota = models.CharField(max_length=200, null=True, blank=True)
    lokasi = models.CharField(max_length=200, null=True, blank=True)

class Table(models.Model):
    kota = models.CharField(max_length=200, null=True, blank=True)
    ciri_khas = models.CharField(max_length=200, null=True, blank=True)
    provinsi = models.CharField(max_length=200, null=True, blank=True)
