from django.conf.urls import include, url
import api.clients.views as views
from compads.router import common_router as router

router.register(r'clients', views.ClientViewSet, base_name='clients')
router.register(r'client-types', views.ClientTypeViewSet, base_name='client_types' )
router.register(r'emails', views.EmailViewSet, base_name='email')
router.register(r'email-types', views.EmailTypeViewSet, base_name='email-types')
router.register(r'phones', views.PhoneViewSet, base_name='phones')
router.register(r'phone-types', views.PhoneTypeViewSet, base_name='phone-types')
router.register(r'addresses', views.AddressViewSet, base_name='addresses')
router.register(r'address-types', views.AddressTypeViewSet, base_name='address-types')
router.register(r'birthdates', views.BirthDateViewSet, base_name='birthdates')

client_detail = views.ClientViewSet.as_view({'get':'retrieve'},lookup_field='pk')
client_type_detail = views.ClientTypeViewSet.as_view({'get':'retrieve'},lookup_field='pk')
client_email_list = views.EmailViewSet.as_view({'get':'list'},lookup_field='pk')
client_phone_list = views.PhoneViewSet.as_view({'get':'list'},lookup_field='pk')
client_address_list = views.AddressViewSet.as_view({'get':'list'},lookup_field='pk')
client_birthdate = views.BirthDateViewSet.as_view({'get':'list'},lookup_field='pk')
email_detail = views.EmailViewSet.as_view({'get':'retrieve'},lookup_field='pk')
email_type_detail = views.EmailTypeViewSet.as_view({'get':'retrieve'},lookup_field='pk')
phone_detail = views.PhoneViewSet.as_view({'get':'retrieve'},lookup_field='pk')
phone_type_detail = views.PhoneTypeViewSet.as_view({'get':'retrieve'},lookup_field='pk')
address_detail = views.AddressViewSet.as_view({'get':'retrieve'},lookup_field='pk')
address_type_detail = views.AddressTypeViewSet.as_view({'get':'retrieve'},lookup_field='pk')
birthdate_detail = views.BirthDateViewSet.as_view({'get':'retrieve'},lookup_field='pk')

urlpatterns = ([
    url(r'^api/clients/(?P<pk>[0-9]+)/$', client_detail , name='client-detail'),
    url(r'^api/client-types/(?P<pk>[0-9]+)/$', client_type_detail, name='client-type-detail'),
    url(r'^api/clients/(?P<pk>[0-9]+)/emails/$', client_email_list, name='client-emails'),
    url(r'^api/clients/(?P<pk>[0-9]+)/phones/$', client_phone_list, name='client-phones'),
    url(r'^api/clients/(?P<pk>[0-9]+)/addresses/$', client_address_list, name='client-addresses'),
    url(r'^api/clients/(?P<pk>[0-9]+)/birthdate/$', client_birthdate, name='client-birthdate'),
    url(r'^api/emails/(?P<pk>[0-9]+)/$', email_detail , name='email-detail'),
    url(r'^api/email-types/(?P<pk>[0-9]+)/$', email_type_detail, name='email-type-detail'),
    url(r'^api/phones/(?P<pk>[0-9]+)/$', phone_detail , name='phone-detail'),
    url(r'^api/phone-types/(?P<pk>[0-9]+)/$', phone_type_detail, name='phone-type-detail'),
    url(r'^api/addresses/(?P<pk>[0-9]+)/$', address_detail , name='address-detail'),
    url(r'^api/address-types/(?P<pk>[0-9]+)/$', address_type_detail, name='address-type-detail'),
    url(r'^api/birthdates/(?P<pk>[0-9]+)/$', birthdate_detail, name='birthdate-detail'),
]);
