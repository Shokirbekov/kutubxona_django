from django.db import models

class Muallif(models.Model):
    ism = models.CharField(max_length=50)
    tirik = models.BooleanField(default=True)
    kitob_soni = models.PositiveSmallIntegerField()
    yosh = models.CharField(max_length=50, blank=True, null=True)
    jins = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self):
        return self.ism

class Talaba(models.Model):
    ism = models.CharField(max_length=50)
    bitiruvchi = models.BooleanField()
    kitoblar_soni = models.PositiveSmallIntegerField(default=0)
    kurs = models.PositiveSmallIntegerField()
    def __str__(self):
        return self.ism
    class Meta:
        ordering = ("ism",)
    
class Admin(models.Model):
    ism = models.CharField(max_length=50)
    ish_vaqti = models.CharField(max_length=50)
    def __str__(self):
        return self.ism

class Kitob(models.Model):
    nom = models.CharField(max_length=100)
    sahifa = models.PositiveSmallIntegerField()
    muallif = models.ForeignKey(Muallif, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.nom}({self.muallif})"
    class Meta:
        ordering = ("id",)

class Record(models.Model):
    talaba = models.ForeignKey(Talaba, on_delete=models.CASCADE)
    kitob = models.ForeignKey(Kitob, on_delete=models.CASCADE)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    olingan_sana = models.DateField()
    qaytarish_sana = models.DateField()
    qaytardi = models.BooleanField()