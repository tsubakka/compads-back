from django.db import models
from django.contrib.auth.models import User
import api.clients.models as clientModels
# Create your models here.

################################################################################

class SzallasTipus(models.Model):
    szallas_tipus = models.TextField(blank=True, null=True)
    class Meta:
        verbose_name = "Szállás típus"
        verbose_name_plural = "Szállás típusok"
    def __unicode__(self):
        return self.szallas_tipus
    def __str__(self):
        return self.szallas_tipus

class SzallasJelleg(models.Model):
    szallas_jelleg = models.TextField(blank=True, null=True)
    class Meta:
        verbose_name = "Szállás jelleg"
        verbose_name_plural = "Szállás jellegek"
    def __unicode__(self):
        return self.szallas_jelleg
    def __str__(self):
        return self.szallas_jelleg

class Szallas(models.Model):
    szallas_nev = models.TextField(blank=False, null=False)
    szallas_cim = models.TextField(blank=False, null=False)
    szallas_tipus = models.ForeignKey(SzallasTipus, on_delete=models.PROTECT)
    szallas_jelleg = models.ForeignKey(SzallasJelleg, on_delete=models.PROTECT)
    class Meta:
        verbose_name = "Szállás"
        verbose_name_plural = "Szállások"
    def __unicode__(self):
        return (self.szallas_nev)
    def __str__(self):
        return (self.szallas_nev)

################################################################################

class SzallasReszTipus(models.Model):
    szallasresz_tipus = models.TextField(blank=True, null=True)
    class Meta:
        verbose_name = "Szállásrész típus"
        verbose_name_plural = "Szállásrész típusok"
    def __unicode__(self):
        return self.szallasresz_tipus
    def __str__(self):
        return self.szallasresz_tipus

class SzallasResz(models.Model):
    szallas = models.ForeignKey(Szallas, on_delete=models.CASCADE, related_name='szallas_szallasreszek')
    szallasresz_tipus = models.ForeignKey(SzallasReszTipus, on_delete=models.PROTECT)
    szallasresz_nev = models.TextField(blank=True, null=True)
    agyak_szama = models.IntegerField(blank=False, null=False)
    potagyak_szama = models.IntegerField(blank=False, null=False)
    szobak_szama = models.IntegerField(blank=False, null=False)
    sajat_konyha = models.BooleanField()
    class Meta:
        verbose_name = "Szállásrész"
        verbose_name_plural = "Szállásrészek"
    def __unicode__(self):
        return '%s - %s - %s' % (self.szallas,self.szallasresz_tipus, self.szallasresz_nev)
    def __str__(self):
        return '%s - %s - %s' % (self.szallas,self.szallasresz_tipus, self.szallasresz_nev)

################################################################################

class AgyTipus(models.Model):
    agy_tipus = models.TextField(blank=False, null=False)
    class Meta:
        verbose_name = "Ágytípus"
        verbose_name_plural = "Ágytípusok"
    def __unicode__(self):
        return (self.agy_tipus)
    def __str__(self):
        return (self.agy_tipus)

################################################################################

class AlapAr(models.Model):
    szallas_tipus = models.ForeignKey(SzallasTipus, on_delete=models.PROTECT)
    agy_tipus = models.ForeignKey(AgyTipus, on_delete=models.PROTECT)
    agy_ar = models.IntegerField(blank=False, null=False)
    class Meta:
        verbose_name = "Alapár"
        verbose_name_plural = "Alapárak"
    def __unicode__(self):
        return '%s - %s - %s' % (self.szallas_tipus,self.agy_tipus, str(self.agy_ar))
    def __str__(self):
        return '%s - %s - %s' % (self.szallas_tipus,self.agy_tipus, str(self.agy_ar))

################################################################################

class Ajanlat(models.Model):
    ajanlatado = models.ForeignKey(User, on_delete=models.PROTECT, related_name='ajanlatado_text')
    ugyfel = models.ForeignKey(clientModels.Client, on_delete=models.PROTECT, related_name='ugyfel')
    erkezes = models.DateTimeField(auto_now=False)
    tavozas = models.DateTimeField(auto_now=False)
    nagykoruak_szama = models.IntegerField(blank=True, null=True)
    ifa = models.IntegerField(blank=True, null=True)
    egyejszakas_felar = models.IntegerField(blank=True, null=True)
    kisallatok_szama = models.IntegerField(blank=True, null=True)
    kisallat_felar_ej = models.IntegerField(blank=True, null=True)
    etkezes_reggeli_db = models.IntegerField(blank=True, null=True)
    etkezes_ebed_db = models.IntegerField(blank=True, null=True)
    etkezes_vacsora_db = models.IntegerField(blank=True, null=True)
    etkezes_reggeli_ar = models.IntegerField(blank=True, null=True)
    etkezes_ebed_ar = models.IntegerField(blank=True, null=True)
    etkezes_vacsora_ar = models.IntegerField(blank=True, null=True)
    etkezes_haromszori_db = models.IntegerField(blank=True, null=True)
    etkezes_haromszori_ar = models.IntegerField(blank=True, null=True)
    etkezes_otszori_db = models.IntegerField(blank=True, null=True)
    etkezes_otszori_ar = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = "Ajánlat"
        verbose_name_plural = "Ajánlatok"

    def __unicode__(self):
        return '%s - %s - %s' % (self.ugyfel,self.erkezes, str(self.tavozas))
    def __str__(self):
        return '%s - %s - %s' % (self.ugyfel,self.erkezes, str(self.tavozas))
################################################################################

class AjanlatResz(models.Model):
    ajanlat = models.ForeignKey(Ajanlat, on_delete=models.PROTECT, related_name='ajanlat_ajanlatreszek')
    szallasresz = models.ForeignKey(SzallasResz, on_delete=models.PROTECT)
    alap_agy_db = models.IntegerField(blank=False, null=False)
    alap_potagy_db = models.IntegerField(blank=True, null=True)
    class Meta:
        verbose_name = "Ajánlatrész"
        verbose_name_plural = "Ajánlatrészek"
    def __unicode__(self):
        return '%s - %s - %s agy, %s potagy' % (self.ajanlat,self.szallasresz, str(self.alap_agy_db) , str(self.alap_potagy_db))
    def __str__(self):
        return '%s - %s - %s agy, %s potagy' % (self.ajanlat,self.szallasresz, str(self.alap_agy_db) , str(self.alap_potagy_db))








################################################################################
