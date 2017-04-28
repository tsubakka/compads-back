from django.conf.urls import include, url
from compads.router import common_router as router
import api.reservations.views as views

router.register(r'szallasok', views.SzallasViewSet, base_name='szallasok')
router.register(r'szallas-tipusok', views.SzallasTipusViewSet, base_name='szallastipusok')
router.register(r'szallas-jellegek', views.SzallasJellegViewSet, base_name='szallasjellegek')
router.register(r'szallasreszek', views.SzallasReszViewSet, base_name='szallasreszek')
router.register(r'szallasresz-tipusok', views.SzallasReszTipusViewSet, base_name='szallasresztipusok')
router.register(r'agy-tipusok', views.AgyTipusViewSet, base_name='agytipusok')
router.register(r'alaparak', views.AlapArViewSet, base_name='alaparak')
router.register(r'ajanlatok', views.AjanlatViewSet, base_name='ajanlatok')
router.register(r'ajanlatreszek', views.AjanlatReszViewSet, base_name='ajanlatreszek')


szallas_detail = views.SzallasViewSet.as_view({'get':'retrieve'},lookup_field='pk')
szallas_szallasresz_list = views.SzallasSzallasReszViewSet.as_view({'get':'list'},lookup_field='pk')
szallas_tipus_detail = views.SzallasTipusViewSet.as_view({'get':'retrieve'},lookup_field='pk')
szallas_jelleg_detail = views.SzallasJellegViewSet.as_view({'get':'retrieve'},lookup_field='pk')
szallasresz_detail = views.SzallasReszViewSet.as_view({'get':'retrieve'},lookup_field='pk')
szallasresz_tipus_detail = views.SzallasReszTipusViewSet.as_view({'get':'retrieve'},lookup_field='pk')
agy_tipus_detail = views.AgyTipusViewSet.as_view({'get':'retrieve'},lookup_field='pk')
alapar_detail = views.AlapArViewSet.as_view({'get':'retrieve'},lookup_field='pk')
ajanlat_detail = views.AjanlatViewSet.as_view({'get':'retrieve'},lookup_field='pk')
ajanlat_ajanlatresz_list = views.AjanlatAjanlatReszViewSet.as_view({'get':'retrieve'},lookup_field='pk')
ajanlatresz_detail = views.AjanlatReszViewSet.as_view({'get':'retrieve'},lookup_field='pk')


urlpatterns=([
    url(r'^api/szallasok/(?P<pk>[0-9]+)/$', szallas_detail , name='szallas-detail'),
    url(r'^api/szallasok/(?P<pk>[0-9]+)/szallasreszek/$', szallas_szallasresz_list , name='szallas-szallasresz-list'),
    url(r'^api/szallas-tipusok/(?P<pk>[0-9]+)/$', szallas_tipus_detail , name='szallas-tipus-detail'),
    url(r'^api/szallas-jellegek/(?P<pk>[0-9]+)/$', szallas_jelleg_detail , name='szallas-jelleg-detail'),
    url(r'^api/szallasreszek/(?P<pk>[0-9]+)/$', szallasresz_detail , name='szallasresz-detail'),
    url(r'^api/szallasresz-tipusok/(?P<pk>[0-9]+)/$', szallasresz_tipus_detail , name='szallasresz-tipus-detail'),
    url(r'^api/agy-tipusok/(?P<pk>[0-9]+)/$', agy_tipus_detail , name='agy-tipus-detail'),
    url(r'^api/alaparak/(?P<pk>[0-9]+)/$', alapar_detail , name='alap-ar-detail'),
    url(r'^api/ajanlatok/(?P<pk>[0-9]+)/$', ajanlat_detail , name='ajanlat-detail'),
    url(r'^api/ajanlatok/(?P<pk>[0-9]+)/ajanlatreszek/$', ajanlat_ajanlatresz_list , name='ajanlat-ajanlatresz-list'),
    url(r'^api/ajanlatreszek/(?P<pk>[0-9]+)/$', ajanlatresz_detail , name='ajanlatresz-detail'),

])
