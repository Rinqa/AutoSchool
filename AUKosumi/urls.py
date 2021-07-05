from django.contrib import admin
from django.urls import path
from Kosumi import views as homeViews
from Kosumi.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as userViews

urlpatterns = [
    path("", home, name="home"),
    path('admin/', admin.site.urls),
    path('Klientat/', homeViews.cli, name="cli"),
    path('Instruktoret/', homeViews.inst, name="ins"),
    path('Instruktor/', homeViews.ins, name="inst"),
    path('signup/', UserRegister, name='sign-up'),
    path('login/', userViews.LoginView.as_view(template_name='home/login.html'), name='login'),
    path('logout/', userViews.LogoutView.as_view(template_name='home/logout.html'), name='logout'),
    path('Klienti/', SearchKlienti, name="klienti_Search"),
    path('klientat/dokTetetehequr/', getDokTerhekur, name="terhequr"),
    path('klientat/dokPatehequr/', getDokPaTerhekur, name="paterhequr"),
    path('Veturat/', vet, name="vet"),
    path('shtoKlientin/', homeViews.shtoKlientin, name="regjistro-klientin"),
    path('shtoInstruktorin/', homeViews.shtoInstruktor, name="regjistro-ins"),
    path('shtoVeturen/', homeViews.shtoVeturen, name="regjistro-vet"),
    path("klieti/editCli/<int:pk>/", editKlienti.as_view(), name="updatecli"),
    path("klieti/terheq/<int:pk>/", terheq.as_view(), name="terheq"),
    path("vetura/<int:pk>/", veturatEdit.as_view(), name="vetura"),
    path("pagesat/<int:pk>/", editPagesen.as_view(), name="editpagesat"),
    path("pagesat/instruktorve/<int:pk>/",
         editPagesenIns.as_view(), name="editpagesatins"),
    path("TerheqDokumentat", ter, name="asd"),
    path("pagesatEinstruktorve/<int:pk>/",
         homeViews.merrPagesat, name="pagesatEins"),
    path("pagesatEinstruktoreve/<int:pk>/",
         homeViews.merrPagesatin, name="pagesatEinst"),
    path("Klientat/<int:pk>/", homeViews.merrGjeneraten, name="gjen"),
    path("shtoPagesenEinstruktorit/",
         homeViews.shtoPagesenIns, name="shtopagesIn"),
    path("shtoPagesat/", homeViews.shtoPagesat, name="shtopagesat"),
    path('pagesatEinstruktorve/', homeViews.pagesatIns, name="pagins"),
    path('pagesat/', homeViews.pagesa, name="pag"),
    path('pages/', homeViews.pages, name="pags"),
    path('Klientat/PaTatim/', homeViews.cliPaTatim, name="patatim"),
    path('FletePagese/',homeViews.pagese,name='krijoPagese'),
]
if (settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
