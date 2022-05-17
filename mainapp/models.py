from django.db import models

class Category(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class SubCategory(models.Model):
    nom = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nom

class Mahsulot(models.Model):
    nom = models.CharField(max_length=100)
    narx = models.IntegerField()
    batafsil = models.TextField()
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nom

class Rasm(models.Model):
    rasm = models.URLField()
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)

class Mijoz(models.Model):
    ism = models.CharField(max_length=100)
    tel = models.CharField(max_length=15)
    tel2 = models.CharField(max_length=15, blank=True)
    manzil = models.CharField(max_length=200)
    qarz = models.IntegerField(default=0)
    qarzdorlik_limit = models.IntegerField(default=100000)

    def __str__(self):
        return f"{self.ism} ({self.tel})"

class Savat(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    mijoz = models.ForeignKey(Mijoz, on_delete=models.CASCADE)

class Buyurtma(models.Model):
    savat = models.ManyToManyField(Savat)
    mijoz = models.ForeignKey(Mijoz, on_delete=models.SET_NULL, null=True)
    umumiy_narx = models.IntegerField()
    yetkazildi = models.BooleanField(default=False)
    berilgan_sana = models.DateTimeField(auto_now_add=True)
    yetkazilgan_sana = models.DateTimeField(auto_now=True)
    tolandi = models.IntegerField()
    haydovchi = models.ForeignKey('adminapp.Haydovchi', on_delete=models.SET_NULL, null=True)




