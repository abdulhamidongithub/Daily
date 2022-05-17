from django.db import models

class Haydovchi(models.Model):
    ism = models.CharField(max_length=100)
    tel = models.CharField(max_length=15)
    qoshilgan_sana = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ism


