from django.db import models
from userapp.models import Ombor

class Mahsulot(models.Model):
    nom = models.CharField(max_length=50)
    brend = models.CharField(max_length=50)
    miqdor = models.SmallIntegerField()
    kelgan_narx = models.IntegerField()
    sotuv_narx = models.IntegerField()
    ombor = models.ForeignKey(Ombor, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nom} ({self.brend})'

class Client(models.Model):
    ism = models.CharField(max_length=50)
    tel = models.CharField(max_length=50)
    dokon = models.CharField(max_length=50)
    manzil = models.CharField(max_length=50)
    qarz = models.IntegerField(default=0)
    ombor = models.ForeignKey(Ombor, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.ism} ({self.dokon})'

