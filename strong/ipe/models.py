from django.db import models

# Create your models here.

class Pengurus(models.Model):
    bph = models.CharField(max_length=70)
    devisi = models.CharField(max_length=75)
    co_anggota = models.CharField(max_length=200)
    departemen = models.CharField(max_length=210)

    def __str__(self):
        return self.bph
    
