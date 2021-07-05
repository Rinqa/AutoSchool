from django.shortcuts import render, redirect
from django.core.files import File
from django.views.generic import UpdateView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from Kosumi.models import Klientat, Instruktori, Veturat, pagesatEinstruktorve, pagesat
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from Kosumi.forms import *

# Create your views here.


class editKlienti(UpdateView):
    model = Klientat
    template_name = 'home/editKlienti.html'
    fields = '__all__'


class terheq(UpdateView):
    model = Klientat
    template_name = 'home/terheqjet.html'
    fields = ['TerheqjaDokumenteve', 'dataTerheqjes']


class veturatEdit(UpdateView):
    model = Veturat
    template_name = "home/editVetura.html"
    fields = '__all__'


class editPagesen(UpdateView):
    model = pagesat
    template_name = 'home/terheqjet.html'
    fields = '__all__'


class editPagesenIns(UpdateView):
    model = pagesatEinstruktorve
    template_name = 'home/terheqjet.html'
    fields = '__all__'


def home(request):
    template_name = "home/home.html"
    return render(request, "home/home.html")

def pagese(request):
    template_name = "home/krijoPages.html"
    return render(request, "home/krijoPages.html")

@login_required
def ter(request):
    kli = Klientat.objects.filter(TerheqjaDokumenteve=False)
    return render(request, "home/test.html", {"kli": kli})


@login_required
def vet(request):
    vet = Veturat.objects.all()
    return render(request, 'home/veturat.html', {'vet': vet})


@login_required
def cli(request):
    kli = kandidatet.objects.all().order_by('-kandatet')
    return render(request, 'home/klientat.html', {'kli': kli})


@login_required
def cliPaTatim(request):
    kli = Klientat.objects.filter(tatimi_id=2)
    return render(request, 'home/kerkoKlientin.html', {"kli": kli})


@login_required
def inst(request):
    ins = Instruktori.objects.all().order_by("id")
    return render(request, "home/inst.html", {"ins": ins})


@login_required
def ins(request):
    ins = Instruktori.objects.all().order_by("id")
    return render(request, "home/ins.html", {"ins": ins})


@login_required
def UserRegister(request):
    if(request.method == 'POST'):
        form = users(request.POST)
        if(form.is_valid()):
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'U krijua faqja per {username}!')
            return redirect('sign-up')
    else:
        form = users()
    return render(request, 'home/signup.html', {'form': form})


@login_required
def SearchKlienti(request):
    query = request.GET.get('q')
    if(query):
        kli = Klientat.objects.filter(Emri__icontains=query)
    elif(query == ''):
        return redirect("home")
    else:
        return redirect("home")
    return render(request, "home/kerkoKlientin.html", {'kli': kli})


@login_required
def getDokTerhekur(request):
    kli = Klientat.objects.filter(TerheqjaDokumenteve=True)
    return render(request, "home/terhequr.html", {"kli": kli})


@login_required
def getDokPaTerhekur(request):
    kli = Klientat.objects.filter(TerheqjaDokumenteve=False)
    return render(request, "home/dokTepaTehekur.html", {"kli": kli})


@login_required
def shtoKlientin(request):
    if request.method == 'POST':
        form = shtoKlient(request.POST)
        if form.is_valid():
            form.save()
            return redirect('regjistro-klientin')
    else:
        form = shtoKlient()
    return render(request, 'home/shtoKlientin.html', {'form': form})


@login_required
def shtoInstruktor(request):
    if request.method == 'POST':
        form = shtoInstruktorin(request.POST)
        if form.is_valid():
            form.save()
            emri = form.cleaned_data.get('emri')
            return redirect('regjistro-ins')
    else:
        form = shtoInstruktorin()
    return render(request, 'home/shtoKlientin.html', {'form': form})


@login_required
def shtoVeturen(request):
    if request.method == "POST":
        form = shtoVetur(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            fotoja = form.cleaned_data.get('fotoja')
            return redirect('vet')
    else:
        form = shtoVetur()
    return render(request, 'home/shtoKlientin.html', {"form": form})


@login_required
def shtoPagesenIns(request):
    if request.method == "POST":
        form = shtoPagesenIn(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pagins')
    else:
        form = shtoPagesenIn()
    return render(request, 'home/shtoKlientin.html', {"form": form})


@login_required
def shtoPagesat(request):
    if request.method == "POST":
        form = shtoPagesen(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pags')
    else:
        form = shtoPagesen()
    return render(request, 'home/shtoKlientin.html', {"form": form})


@login_required
def merrPagesat(request, pk):
    pag = pagesatEinstruktorve.objects.filter(Instruktori_id=pk)
    return render(request, "home/pagesatEinstruktorve.html", {'pag': pag})


def merrPagesatin(request, pk):
    pag = pagesatEinstruktorve.objects.filter(Instruktori_id=pk)
    return render(request, "home/pagesatInsDow.html", {'pag': pag})


def merrGjeneraten(request, pk):
    orderbyList = ['nr', 'Kursi']
    gjen = Klientat.objects.filter(kandidatet_id=pk).order_by(*orderbyList)
    return render(request, 'home/gjenKlientave.html', {'gjen': gjen})


@login_required
def pagesatIns(request):
    pag = pagesatEinstruktorve.objects.all().order_by("muaji")
    return render(request, 'home/pagesatEinstruktorve.html', {'pag': pag})


@login_required
def pagesa(request):
    pag = pagesat.objects.all().order_by('viti')
    return render(request, 'home/pagesat.html', {'pag': pag})


@login_required
def pages(request):
    pag = pagesat.objects.all().order_by('viti')
    return render(request, 'home/pages.html', {'pag': pag})
