from django.db import models




class Managemen(models.Model):
    organisasi = models.CharField(max_length=40)
    Pemimpin = models.CharField(max_length=75)
    
    def __str__(self):
        return self.organisasi


     

# Create your models here.
