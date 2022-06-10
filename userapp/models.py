from django.contrib.auth.models import User
from django.db import models

class Ombor(models.Model):
    ism = models.CharField(max_length=50)
    tel = models.CharField(max_length=50)
    dokon = models.CharField(max_length=50)
    manzil = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.ism} ({self.dokon})"
