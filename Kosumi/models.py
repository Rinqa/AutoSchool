from django.db import models
from django.db.models.base import Model
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime
from django.urls import reverse
from PIL import Image

# Create your models here.
class kandidatet(models.Model):
    kandatet = models.IntegerField(default=datetime.now().year)
    def __str__(self):
        return str(self.kandatet)
class Veturat(models.Model):
    KategoriaMjetit = models.CharField(max_length=10)
    Modeli = models.CharField(max_length=50)
    NriAtestit = models.CharField(max_length=50)
    NrVRC = models.IntegerField()
    targat = models.CharField(max_length=50)
    dataRegjistrimit = models.DateField()
    dataKalimitTeRegjistrimit = models.DateField()
    fotoja = models.ImageField(null=True)
    def __str__(self):
        return  self.Modeli
    def get_absolute_url(self):
        return reverse('vet')
class Instruktori(models.Model):
    Emri = models.CharField(max_length=50)
    Emri_Prindit = models.CharField(max_length=50,default="")
    Mbiemri = models.CharField(max_length=50)
    nrLicenses = models.CharField(max_length=50,null=True)
    dataLindjes = models.DateField(null=True)
    NrPersonal = models.IntegerField(null=True)
    komuna = models.CharField(max_length=50,null=True)
    Nr_tel = PhoneNumberField()
    vetura = models.ForeignKey(Veturat,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return self.Emri+" "+self.Mbiemri

class tat(models.Model):
    tat = models.CharField(max_length=5)
    def __str__(self):
        return self.tat
class Klientat(models.Model):
    nr  = models.IntegerField()
    Emri = models.CharField(max_length=50)
    Emri_Prindit = models.CharField(max_length=50,default="")
    Mbiemri = models.CharField(max_length=50)
    NrPersonal = models.IntegerField()
    DataLindjes = models.DateField(default=datetime.now)
    kandidatet = models.ForeignKey(kandidatet,on_delete=models.CASCADE,null=True)
    Qmimi_Regjistrimit = models.IntegerField(default=0)
    numriOreve = models.IntegerField(default=20)
    borgj = models.FloatField(default=0)
    Instruktori = models.ForeignKey(Instruktori,on_delete=models.CASCADE)
    Vendbanimi = models.CharField(max_length=100)
    NrTelefonit = PhoneNumberField()
    Kursi = models.IntegerField(default=0)
    data_Regjistrimit = models.DateField(default=datetime.now)
    tatimi = models.ForeignKey(tat,on_delete=models.CASCADE, default=2)
    TerheqjaDokumenteve = models.BooleanField(default=False)
    Vijimi = models.BooleanField(default=True)
    dataTerheqjes = models.DateField(null=True,blank=True)
    pagesaNeBank = models.CharField(max_length=2,default="Jo")

    def __str__(self):
        return self.Emri +" "+ self.Emri_Prindit+" "+self.Mbiemri
    def get_absolute_url(self):
        return reverse('cli')
        

class muaji(models.Model):
    muaji = models.CharField(max_length=50)
    def __str__(self):
        return self.muaji
class pagesat(models.Model):
    muaji = models.ForeignKey(muaji,on_delete=models.CASCADE)
    kontabilisti = models.FloatField()
    poligoni = models.FloatField()
    qeraja = models.FloatField()
    rryma = models.FloatField()
    ligjerusi = models.FloatField()
    Kontributet = models.FloatField()
    Administrata = models.IntegerField(default=0)
    viti = models.IntegerField(default=datetime.now().year)
    
    def __str__(self):
        return str(self.muaji)+"/"+str(self.viti)

    def get_absolute_url(self):
        return reverse('pags')
class pagesatEinstruktorve(models.Model):
    Instruktori = models.ForeignKey(Instruktori,on_delete=models.CASCADE)
    muaji  = models.ForeignKey(muaji,on_delete=models.CASCADE)
    paga = models.FloatField()
    viti = models.IntegerField(default=datetime.now().year)
    def __str__(self):
        return str(self.Instruktori)+ " "+ str(self.muaji)+ " "+str(self.paga)

    def get_absolute_url(self):
        return reverse('pagins')
    

class Voizitja(models.Model):
    Nr  = models.IntegerField()
    Emri = models.CharField(max_length=500)
    Data = models.DateField()
    Ora = models.TimeField()
    Pagesa = models.IntegerField()
    Statusi = models.CharField(max_length=100)
    PjesetNeHyrje = models.IntegerField()

    def __str__(self):
        return self.Emri+ " " + str(self.Data) +" " + str(self.Ora)
    def get_absolute_url(self):
        return reverse('voz')



