from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import*
from django.views.generic import UpdateView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy


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


class shtoKlient(forms.ModelForm):
    class Meta:
        model = Klientat
        widgets = {
            'DataLindjes': forms.DateInput(attrs={'placeholder': 'Name'}),

        }
        fields = '__all__'

class shtoVetur(forms.ModelForm):
    class Meta:
        model = Veturat
        fields = ['KategoriaMjetit','Modeli','NriAtestit','NrVRC','targat','dataRegjistrimit','dataKalimitTeRegjistrimit','fotoja']

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
