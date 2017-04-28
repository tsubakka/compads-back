from django.contrib import admin
import api.reservations.models as models

admin.site.register(models.Szallas)
admin.site.register(models.SzallasTipus)
admin.site.register(models.SzallasJelleg)
admin.site.register(models.SzallasResz)
admin.site.register(models.SzallasReszTipus)
admin.site.register(models.AgyTipus)
admin.site.register(models.AlapAr)
admin.site.register(models.Ajanlat)
admin.site.register(models.AjanlatResz)
