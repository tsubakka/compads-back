from rest_framework.response import Response
import rest_framework.filters as filters
import rest_framework.permissions as permissions
import rest_framework.generics as generics
from  rest_framework import viewsets

import api.pagination as pagination

import api.reservations.serializers as serializers
import api.reservations.models as models

################################################################################

class SzallasViewSet(viewsets.ModelViewSet):
    queryset = models.Szallas.objects.all()
    serializer_class = serializers.SzallasSerializer
    pagination_class = pagination.DefaultPageNumberPagination #PageNumberPagination
    filter_backends= [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['szallas_nev']
    permission_classes = [permissions.IsAuthenticated]

################################################################################

class SzallasJellegViewSet(viewsets.ModelViewSet):
    queryset = models.SzallasJelleg.objects.all()
    serializer_class = serializers.SzallasJellegSerializer
    pagination_class = pagination.DefaultPageNumberPagination #PageNumberPagination
    filter_backends= [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['szallas_jelleg']
    permission_classes = [permissions.IsAuthenticated]

################################################################################

class SzallasTipusViewSet(viewsets.ModelViewSet):
    queryset = models.SzallasTipus.objects.all()
    serializer_class = serializers.SzallasTipusSerializer
    pagination_class = pagination.DefaultPageNumberPagination #PageNumberPagination
    filter_backends= [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['szallas_tipus']
    permission_classes = [permissions.IsAuthenticated]

################################################################################

class SzallasSzallasReszViewSet(viewsets.ModelViewSet):
    queryset = models.SzallasResz.objects.all()
    serializer_class = serializers.SzallasReszSerializer
    pagination_class = pagination.DefaultPageNumberPagination #PageNumberPagination
    filter_backends= [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['szallasresz_nev']
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self, *args, **kwargs):
        queryset =  models.SzallasResz.objects.all()
        if 'pk' in self.kwargs:
            queryset = models.SzallasResz.objects.filter(szallas_id=self.kwargs['pk'])
        return queryset


################################################################################

class SzallasReszTipusViewSet(viewsets.ModelViewSet):
    queryset = models.SzallasReszTipus.objects.all()
    serializer_class = serializers.SzallasReszTipusSerializer
    pagination_class = pagination.DefaultPageNumberPagination #PageNumberPagination
    filter_backends= [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['szallasresz_tipus']
    permission_classes = [permissions.IsAuthenticated]

################################################################################

class SzallasReszViewSet(viewsets.ModelViewSet):
    queryset = models.SzallasResz.objects.all()
    serializer_class = serializers.SzallasReszSerializer
    pagination_class = pagination.DefaultPageNumberPagination #PageNumberPagination
    filter_backends= [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['szallasresz_nev']
    permission_classes = [permissions.IsAuthenticated]

################################################################################

class AgyTipusViewSet(viewsets.ModelViewSet):
    queryset = models.AgyTipus.objects.all()
    serializer_class = serializers.AgyTipusSerializer
    pagination_class = pagination.DefaultPageNumberPagination #PageNumberPagination
    filter_backends= [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['agy_tipus']
    permission_classes = [permissions.IsAuthenticated]

################################################################################

class AlapArViewSet(viewsets.ModelViewSet):
    queryset = models.AlapAr.objects.all()
    serializer_class = serializers.AlapArSerializer
    pagination_class = pagination.DefaultPageNumberPagination #PageNumberPagination
    filter_backends= [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['agy_ar']
    permission_classes = [permissions.IsAuthenticated]

################################################################################

class AjanlatAjanlatReszViewSet(viewsets.ModelViewSet):
    queryset = models.AjanlatResz.objects.all()
    serializer_class = serializers.AjanlatReszSerializer
    pagination_class = pagination.DefaultPageNumberPagination #PageNumberPagination
    filter_backends= [filters.SearchFilter, filters.OrderingFilter]
    #search_fields = ['szallasresz_nev']
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self, *args, **kwargs):
        queryset =  models.AjanlatResz.objects.all()
        if 'pk' in self.kwargs:
            queryset = models.AjanlatResz.objects.filter(ajanlat_id=self.kwargs['pk'])
        return queryset

class AjanlatReszViewSet(viewsets.ModelViewSet):
    queryset = models.AjanlatResz.objects.all()
    serializer_class = serializers.AjanlatReszSerializer
    pagination_class = pagination.DefaultPageNumberPagination #PageNumberPagination
    filter_backends= [filters.SearchFilter, filters.OrderingFilter]
    #search_fields = ['szallasresz_nev']
    permission_classes = [permissions.IsAuthenticated]

class AjanlatViewSet(viewsets.ModelViewSet):
    queryset = models.Ajanlat.objects.all()
    serializer_class = serializers.AjanlatSerializer
    pagination_class = pagination.DefaultPageNumberPagination #PageNumberPagination
    filter_backends= [filters.SearchFilter, filters.OrderingFilter]
    #search_fields = ['szallasresz_nev']
    permission_classes = [permissions.IsAuthenticated]

































################################################################################
