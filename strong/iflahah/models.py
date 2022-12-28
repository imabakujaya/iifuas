from django.db import models




class Rutinitas(models.Model):
    istighosah = models.CharField(max_length=30)
    kajian = models.CharField(max_length=30)
    
    def __str__(self):
        return self.istighosah


# Create your models here.
