from django.contrib import admin

from Kosumi.views import vozitja
from .models import*
# Register your models here.
admin.site.register(Klientat)
admin.site.register(Instruktori)
admin.site.register(tat)
admin.site.register(pagesat)
admin.site.register(muaji)
admin.site.register(Veturat)
admin.site.register(pagesatEinstruktorve)
admin.site.register(kandidatet)
admin.site.register(Voizitja)


