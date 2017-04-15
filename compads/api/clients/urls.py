from django.conf.urls import include, url

import api.clients.views as views

urlpatterns = ([

    url(r'^$', views.ClientListAPIView.as_view(), name='client-list'),
    url(r'^(?P<pk>[0-9]+)/$', views.ClientDetailAPIView.as_view(), name='client-detail'),
    url(r'^create/$', views.ClientCreateAPIView.as_view(), name='client-create'),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.ClientUpdateAPIView.as_view(), name='client-update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.ClientDeleteAPIView.as_view(), name='client-delete'),
    url(r'^(?P<pk>[0-9]+)/emails/$', views.ClientEmailListAPIView.as_view(), name='client-emails'),
    url(r'^(?P<pk>[0-9]+)/phones/$', views.ClientPhoneListAPIView.as_view(), name='client-phones'),
    url(r'^(?P<pk>[0-9]+)/addresses/$', views.ClientAddressListAPIView.as_view(), name='client-addresses'),
    url(r'^(?P<pk>[0-9]+)/birthdate/$', views.ClientBirthDateAPIView.as_view(), name='client-birthdate'),

    url(r'^client-types/$', views.ClientTypeListAPIView.as_view(), name="client-type-list"),#, namespace='users-api')),
    url(r'^client-types/create/$', views.ClientTypeCreateAPIView.as_view(), name='client-type-create'),
    url(r'^client-types/(?P<pk>[0-9]+)/$', views.ClientTypeDetailAPIView.as_view(), name='client-type-detail'),
    url(r'^client-types/(?P<pk>[0-9]+)/edit/$', views.ClientTypeUpdateAPIView.as_view(), name='client-type-update'),
    url(r'^client-types/(?P<pk>[0-9]+)/delete/$', views.ClientTypeDeleteAPIView.as_view(), name='client-type-delete'),

    url(r'^birthdates/$', views.BirthDateListAPIView.as_view(), name='birthdate-list'),
    url(r'^birthdates/(?P<pk>[0-9]+)/$', views.BirthDateDetailAPIView.as_view(), name='birthdate-detail'),
    url(r'^birthdates/create/$', views.BirthDateCreateAPIView.as_view(), name='birthdate-create'),
    url(r'^birthdates/(?P<pk>[0-9]+)/edit/$', views.BirthDateUpdateAPIView.as_view(), name='birthdate-update'),
    url(r'^birthdates/(?P<pk>[0-9]+)/delete/$', views.BirthDateDeleteAPIView.as_view(), name='birthdate-delete'),

    url(r'^phones/$', views.PhoneListAPIView.as_view(), name='phone-list'),
    url(r'^phones/(?P<pk>[0-9]+)/$', views.PhoneDetailAPIView.as_view(), name='phone-detail'),
    url(r'^phones/create/$', views.PhoneCreateAPIView.as_view(), name='phone-create'),
    url(r'^phones/(?P<pk>[0-9]+)/edit/$', views.PhoneUpdateAPIView.as_view(), name='phone-update'),
    url(r'^phones/(?P<pk>[0-9]+)/delete/$', views.PhoneDeleteAPIView.as_view(), name='phone-delete'),

    url(r'^phone-types/$', views.PhoneTypeListAPIView.as_view(), name='phone-type-list'),
    url(r'^phone-types/(?P<pk>[0-9]+)/$', views.PhoneTypeDetailAPIView.as_view(), name='phone-type-detail'),
    url(r'^phone-types/create/$', views.PhoneTypeCreateAPIView.as_view(), name='phone-type-create'),
    url(r'^phone-types/(?P<pk>[0-9]+)/edit/$', views.PhoneTypeUpdateAPIView.as_view(), name='phone-type-update'),
    url(r'^phone-types/(?P<pk>[0-9]+)/delete/$', views.PhoneTypeDeleteAPIView.as_view(), name='phone-type-delete'),

    url(r'^emails/$', views.EmailListAPIView.as_view(), name='email-list'),
    url(r'^emails/(?P<pk>[0-9]+)/$', views.EmailDetailAPIView.as_view(), name='email-detail'),
    url(r'^emails/create/$', views.EmailCreateAPIView.as_view(), name='email-create'),
    url(r'^emails/(?P<pk>[0-9]+)/edit/$', views.EmailUpdateAPIView.as_view(), name='email-update'),
    url(r'^emails/(?P<pk>[0-9]+)/delete/$', views.EmailDeleteAPIView.as_view(), name='email-delete'),

    url(r'^email-types/$', views.EmailTypeListAPIView.as_view(), name='email-type-list'),
    url(r'^email-types/(?P<pk>[0-9]+)/$', views.EmailTypeDetailAPIView.as_view(), name='email-type-detail'),
    url(r'^email-types/create/$', views.EmailTypeCreateAPIView.as_view(), name='email-type-create'),
    url(r'^email-types/(?P<pk>[0-9]+)/edit/$', views.EmailTypeUpdateAPIView.as_view(), name='email-type-update'),
    url(r'^email-types/(?P<pk>[0-9]+)/delete/$', views.EmailTypeDeleteAPIView.as_view(), name='email-type-delete'),

    url(r'^addresses/$', views.AddressListAPIView.as_view(), name='address-list'),
    url(r'^addresses/(?P<pk>[0-9]+)/$', views.AddressDetailAPIView.as_view(), name='address-detail'),
    url(r'^addresses/create/$', views.AddressCreateAPIView.as_view(), name='address-create'),
    url(r'^addresses/(?P<pk>[0-9]+)/edit/$', views.AddressUpdateAPIView.as_view(), name='address-update'),
    url(r'^addresses/(?P<pk>[0-9]+)/delete/$', views.AddressDeleteAPIView.as_view(), name='address-delete'),

    url(r'^address-types/$', views.AddressTypeListAPIView.as_view(), name='address-type-list'),
    url(r'^address-types/(?P<pk>[0-9]+)/$', views.AddressTypeDetailAPIView.as_view(), name='address-type-detail'),
    url(r'^address-types/create/$', views.AddressTypeCreateAPIView.as_view(), name='address-type-create'),
    url(r'^address-types/(?P<pk>[0-9]+)/edit/$', views.AddressTypeUpdateAPIView.as_view(), name='address-type-update'),
    url(r'^address-types/(?P<pk>[0-9]+)/delete/$', views.AddressTypeDeleteAPIView.as_view(), name='address-type-delete'),

])
