from django.db.models import Q

from rest_framework.response import Response
import rest_framework.filters as filters
import rest_framework.permissions as permissions
import rest_framework.generics as generics
from  rest_framework import viewsets

import api.pagination as pagination

import api.clients.serializers as serializers
import api.clients.models as models

################################################################################

class ClientViewSet(viewsets.ModelViewSet):
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer
    pagination_class = pagination.DefaultPageNumberPagination #PageNumberPagination
    filter_backends= [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['first_name','last_name','company_name']
    permission_classes = [permissions.IsAuthenticated]

################################################################################

class ClientTypeViewSet(viewsets.ModelViewSet):
    queryset = models.ClientType.objects.all()
    serializer_class = serializers.ClientTypeSerializer
    pagination_class = pagination.DefaultPageNumberPagination #PageNumberPagination
    filter_backends= [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['client_type']
    permission_classes = [permissions.IsAuthenticated]

################################################################################

class EmailViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EmailSerializer
    pagination_class = pagination.DefaultPageNumberPagination #PageNumberPagination
    filter_backends= [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['email_address']
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self, *args, **kwargs):
        queryset =  models.Email.objects.all()
        if 'pk' in self.kwargs:
            queryset = models.Email.objects.filter(client_id=self.kwargs['pk'])
        return queryset

################################################################################

class EmailTypeViewSet(viewsets.ModelViewSet):
    queryset = models.EmailType.objects.all()
    serializer_class = serializers.EmailTypeSerializer
    filter_backends= [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['email_type']
    permission_classes = [permissions.IsAuthenticated]

################################################################################

class PhoneViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PhoneSerializer
    filter_backends= [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['phone_number', 'area_code', 'country_code']
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self, *args, **kwargs):
        queryset =  models.Phone.objects.all()
        if 'pk' in self.kwargs:
            queryset = models.Phone.objects.filter(client_id=self.kwargs['pk'])
        return queryset

################################################################################

class PhoneTypeViewSet(viewsets.ModelViewSet):
    queryset = models.PhoneType.objects.all()
    serializer_class = serializers.PhoneTypeSerializer
    filter_backends= [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['phone_type']
    permission_classes = [permissions.IsAuthenticated]

################################################################################

class AddressViewSet(viewsets.ModelViewSet):
    queryset = models.Address.objects.all()
    serializer_class = serializers.AddressSerializer
    filter_backends= [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['country','region','station','zip_code','address1','address2']
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self, *args, **kwargs):
        queryset =  models.Address.objects.all()
        if 'pk' in self.kwargs:
            queryset = models.Address.objects.filter(client_id=self.kwargs['pk'])
        return queryset

################################################################################

class AddressTypeViewSet(viewsets.ModelViewSet):
    queryset = models.AddressType.objects.all()
    serializer_class = serializers.AddressTypeSerializer
    filter_backends= [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['address_type']
    permission_classes = [permissions.IsAuthenticated]

################################################################################

class BirthDateViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BirthDateSerializer
    filter_backends= [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['year','month','day']
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self, *args, **kwargs):
        queryset =  models.BirthDate.objects.all()
        if 'pk' in self.kwargs:
            queryset = models.BirthDate.objects.filter(client_id=self.kwargs['pk'])
        return queryset

################################################################################





"""
    def get_queryset(self, *args, **kwargs):
        #queryset_list = super(PostListAPIView, self).get_queryset(*args, **kwargs)
        queryset_list = models.BirthDate.objects.all() #filter(user=self.request.user)
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                    Q(BirthDate_type__icontains=query)#|
                #    Q(content__icontains=query)|
                #    Q(user__first_name__icontains=query) |
                #    Q(user__last_name__icontains=query)
                    ).distinct()
        return queryset_list
"""
