from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.models import fields
from django.forms import widgets
from .models import*
from django.views.generic import UpdateView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'
class users(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'password1', 'password2']


class terheq(forms.ModelForm):
    class Meta:
        model = Klientat
        TerheqjaDokumenteve = forms.BooleanField(initial=True)
        fields = ['dataTerheqjes']
        widgets={"dataTerheqjes":DateInput()}


class shtoKlient(forms.ModelForm):
    class Meta:
        model = Klientat
        
        fields = '__all__'
        widgets = {"DataLindjes":DateInput(),"data_Regjistrimit":DateInput()}

class shtoVetur(forms.ModelForm):
    class Meta:
        model = Veturat
        fields = ['KategoriaMjetit','Modeli','NriAtestit','NrVRC','targat','dataRegjistrimit','dataKalimitTeRegjistrimit','fotoja']
        widgets = {"dataRegjistrimit":DateInput(),"dataKalimitTeRegjistrimit":DateInput()}
class shtoPagesenIn(forms.ModelForm):
    class Meta:
        model = pagesatEinstruktorve
        fields='__all__'

class shtoPagesen(forms.ModelForm):
    class Meta:
        model = pagesat
        fields='__all__'
class shtoInstruktorin(forms.ModelForm):
    class Meta:
        model = Instruktori
        fields = '__all__'
        widgets={"dataLindjes":DateInput()}
class shtoVozitjen(forms.ModelForm):
    class Meta:
        model = Voizitja
        fields = '__all__'
        widgets = {'Data':DateInput(),'Ora':TimeInput()}
    