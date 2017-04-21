from django.db.models import Q

from rest_framework.response import Response

import rest_framework.filters as filters

import rest_framework.permissions as permissions

import rest_framework.generics as generics

import api.pagination as pagination

from .permissions import IsOwnerOrReadOnly

import api.clients.serializers as serializers

import api.clients.models as models

################################################################################

class ClientTypeListAPIView(generics.ListAPIView):
    serializer_class = serializers.ClientTypeListSerializer
    filter_backends= [filters.SearchFilter, filters.OrderingFilter]
    permission_classes = [permissions.IsAuthenticated]
    search_fields = ['client_type',]
    pagination_class = pagination.DefaultPageNumberPagination #PageNumberPagination
    def get_queryset(self, *args, **kwargs):
        #queryset_list = super(PostListAPIView, self).get_queryset(*args, **kwargs)
        queryset_list = models.ClientType.objects.all() #filter(user=self.request.user)
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                    Q(client_type__icontains=query)#|
                #    Q(content__icontains=query)|
                #    Q(user__first_name__icontains=query) |
                #    Q(user__last_name__icontains=query)
                    ).distinct()
        return queryset_list

class ClientTypeCreateAPIView(generics.CreateAPIView):
    queryset = models.ClientType.objects.all()
    serializer_class = serializers.ClientTypeCreateUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]
    #def perform_create(self, serializer):
    #    serializer.save(user=self.request.user)

class ClientTypeDetailAPIView(generics.RetrieveAPIView):
    queryset = models.ClientType.objects.all()
    serializer_class = serializers.ClientTypeDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

class ClientTypeUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = models.ClientType.objects.all()
    serializer_class = serializers.ClientTypeCreateUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

class ClientTypeDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = models.ClientType.objects.all()
    serializer_class = serializers.ClientTypeDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

################################################################################

class ClientListAPIView(generics.ListAPIView):
    serializer_class = serializers.ClientListSerializer
    filter_backends= [filters.SearchFilter, filters.OrderingFilter]
    permission_classes = [permissions.IsAuthenticated]
    search_fields = ['first_name','last_name','company_name']
    pagination_class = pagination.DefaultPageNumberPagination #PageNumberPagination

    def get_queryset(self, *args, **kwargs):
        #queryset_list = super(PostListAPIView, self).get_queryset(*args, **kwargs)
        queryset_list = models.Client.objects.all() #filter(user=self.request.user)
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                    Q(client_type__icontains=query)#|
                #    Q(content__icontains=query)|
                #    Q(user__first_name__icontains=query) |
                #    Q(user__last_name__icontains=query)
                    ).distinct()
        return queryset_list

class ClientDetailAPIView(generics.RetrieveAPIView):
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

class ClientCreateAPIView(generics.CreateAPIView):
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientCreateUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

class ClientUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientCreateUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

class ClientDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

class ClientEmailListAPIView(generics.ListAPIView):
    #queryset = models.Email.objects.all()
    serializer_class = serializers.EmailListSerializer
    permission_classes = [permissions.IsAuthenticated]
    #lookup_field='pk'
    def get_queryset(self):
        return models.Email.objects.filter(client_id=self.kwargs['pk'])

class ClientPhoneListAPIView(generics.ListAPIView):
    #queryset = models.Phone.objects.all()
    serializer_class = serializers.PhoneListSerializer
    permission_classes = [permissions.IsAuthenticated]
    #lookup_field='pk'
    def get_queryset(self):
        return models.Phone.objects.filter(client_id=self.kwargs['pk'])

class ClientAddressListAPIView(generics.ListAPIView):
    #queryset = models.Address.objects.all()
    serializer_class = serializers.AddressListSerializer
    permission_classes = [permissions.IsAuthenticated]
    #lookup_field='pk'
    def get_queryset(self):
        return models.Address.objects.filter(client_id=self.kwargs['pk'])

class ClientBirthDateAPIView(generics.ListAPIView):
    #queryset = models.Address.objects.all()
    serializer_class = serializers.BirthDateListSerializer
    permission_classes = [permissions.IsAuthenticated]
    #lookup_field='pk'
    def get_queryset(self):
        return models.BirthDate.objects.filter(client_id=self.kwargs['pk'])

################################################################################

class PhoneListAPIView(generics.ListAPIView):
    serializer_class = serializers.PhoneListSerializer
    filter_backends= [filters.SearchFilter, filters.OrderingFilter]
    permission_classes = [permissions.IsAuthenticated]
    search_fields = ['first_name','last_name','company_name']
    pagination_class = pagination.DefaultPageNumberPagination #PageNumberPagination
    def get_queryset(self, *args, **kwargs):
        #queryset_list = super(PostListAPIView, self).get_queryset(*args, **kwargs)
        queryset_list = models.Phone.objects.all() #filter(user=self.request.user)
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                    Q(client_type__icontains=query)#|
                #    Q(content__icontains=query)|
                #    Q(user__first_name__icontains=query) |
                #    Q(user__last_name__icontains=query)
                    ).distinct()
        return queryset_list

class PhoneDetailAPIView(generics.RetrieveAPIView):
    queryset = models.Phone.objects.all()
    serializer_class = serializers.PhoneDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

class PhoneCreateAPIView(generics.CreateAPIView):
    queryset = models.Phone.objects.all()
    serializer_class = serializers.PhoneCreateUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

class PhoneUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = models.Phone.objects.all()
    serializer_class = serializers.PhoneCreateUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

class PhoneDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = models.Phone.objects.all()
    serializer_class = serializers.PhoneDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

################################################################################

class PhoneTypeListAPIView(generics.ListAPIView):
    serializer_class = serializers.PhoneTypeListSerializer
    filter_backends= [filters.SearchFilter, filters.OrderingFilter]
    permission_classes = [permissions.IsAuthenticated]
    search_fields = ['first_name','last_name','company_name']
    pagination_class = pagination.DefaultPageNumberPagination #PageNumberPagination

    def get_queryset(self, *args, **kwargs):
        #queryset_list = super(PostListAPIView, self).get_queryset(*args, **kwargs)
        queryset_list = models.PhoneType.objects.all() #filter(user=self.request.user)
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                    Q(client_type__icontains=query)#|
                #    Q(content__icontains=query)|
                #    Q(user__first_name__icontains=query) |
                #    Q(user__last_name__icontains=query)
                    ).distinct()
        return queryset_list

class PhoneTypeDetailAPIView(generics.RetrieveAPIView):
    queryset = models.PhoneType.objects.all()
    serializer_class = serializers.PhoneTypeDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

class PhoneTypeCreateAPIView(generics.CreateAPIView):
    queryset = models.PhoneType.objects.all()
    serializer_class = serializers.PhoneTypeCreateUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

class PhoneTypeUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = models.PhoneType.objects.all()
    serializer_class = serializers.PhoneTypeCreateUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

class PhoneTypeDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = models.PhoneType.objects.all()
    serializer_class = serializers.PhoneTypeDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

################################################################################

class EmailListAPIView(generics.ListAPIView):
    serializer_class = serializers.EmailListSerializer
    filter_backends= [filters.SearchFilter, filters.OrderingFilter]
    permission_classes = [permissions.IsAuthenticated]
    search_fields = ['email_address']
    pagination_class = pagination.DefaultPageNumberPagination #PageNumberPagination

    def get_queryset(self, *args, **kwargs):
        #queryset_list = super(PostListAPIView, self).get_queryset(*args, **kwargs)
        queryset_list = models.Email.objects.all() #filter(user=self.request.user)
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                    Q(client_type__icontains=query)#|
                #    Q(content__icontains=query)|
                #    Q(user__first_name__icontains=query) |
                #    Q(user__last_name__icontains=query)
                    ).distinct()
        return queryset_list

class EmailDetailAPIView(generics.RetrieveAPIView):
    queryset = models.Email.objects.all()
    serializer_class = serializers.EmailDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

class EmailCreateAPIView(generics.CreateAPIView):
    queryset = models.Email.objects.all()
    serializer_class = serializers.EmailCreateUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

class EmailUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = models.Email.objects.all()
    serializer_class = serializers.EmailCreateUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

class EmailDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = models.Email.objects.all()
    serializer_class = serializers.EmailDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

################################################################################

class EmailTypeListAPIView(generics.ListAPIView):
    serializer_class = serializers.EmailTypeListSerializer
    filter_backends= [filters.SearchFilter, filters.OrderingFilter]
    permission_classes = [permissions.IsAuthenticated]
    search_fields = ['first_name','last_name','company_name']
    pagination_class = pagination.DefaultPageNumberPagination #PageNumberPagination

    def get_queryset(self, *args, **kwargs):
        #queryset_list = super(PostListAPIView, self).get_queryset(*args, **kwargs)
        queryset_list = models.EmailType.objects.all() #filter(user=self.request.user)
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                    Q(client_type__icontains=query)#|
                #    Q(content__icontains=query)|
                #    Q(user__first_name__icontains=query) |
                #    Q(user__last_name__icontains=query)
                    ).distinct()
        return queryset_list

class EmailTypeDetailAPIView(generics.RetrieveAPIView):
    queryset = models.EmailType.objects.all()
    serializer_class = serializers.EmailTypeDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

class EmailTypeCreateAPIView(generics.CreateAPIView):
    queryset = models.EmailType.objects.all()
    serializer_class = serializers.EmailTypeCreateUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

class EmailTypeUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = models.EmailType.objects.all()
    serializer_class = serializers.EmailTypeCreateUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

class EmailTypeDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = models.EmailType.objects.all()
    serializer_class = serializers.EmailTypeDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

################################################################################

class AddressTypeListAPIView(generics.ListAPIView):
    serializer_class = serializers.AddressTypeListSerializer
    filter_backends= [filters.SearchFilter, filters.OrderingFilter]
    permission_classes = [permissions.IsAuthenticated]
    search_fields = ['first_name','last_name','company_name']
    pagination_class = pagination.DefaultPageNumberPagination #PageNumberPagination

    def get_queryset(self, *args, **kwargs):
        #queryset_list = super(PostListAPIView, self).get_queryset(*args, **kwargs)
        queryset_list = models.AddressType.objects.all() #filter(user=self.request.user)
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                    Q(AddressType_type__icontains=query)#|
                #    Q(content__icontains=query)|
                #    Q(user__first_name__icontains=query) |
                #    Q(user__last_name__icontains=query)
                    ).distinct()
        return queryset_list

class AddressTypeDetailAPIView(generics.RetrieveAPIView):
    queryset = models.AddressType.objects.all()
    serializer_class = serializers.AddressTypeDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

class AddressTypeCreateAPIView(generics.CreateAPIView):
    queryset = models.AddressType.objects.all()
    serializer_class = serializers.AddressTypeCreateUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

class AddressTypeUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = models.AddressType.objects.all()
    serializer_class = serializers.AddressTypeCreateUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

class AddressTypeDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = models.AddressType.objects.all()
    serializer_class = serializers.AddressTypeDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

################################################################################

class AddressListAPIView(generics.ListAPIView):
    serializer_class = serializers.AddressListSerializer
    filter_backends= [filters.SearchFilter, filters.OrderingFilter]
    permission_classes = [permissions.IsAuthenticated]
    search_fields = ['first_name','last_name','company_name']
    pagination_class = pagination.DefaultPageNumberPagination #PageNumberPagination

    def get_queryset(self, *args, **kwargs):
        #queryset_list = super(PostListAPIView, self).get_queryset(*args, **kwargs)
        queryset_list = models.Address.objects.all() #filter(user=self.request.user)
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                    Q(Address_type__icontains=query)#|
                #    Q(content__icontains=query)|
                #    Q(user__first_name__icontains=query) |
                #    Q(user__last_name__icontains=query)
                    ).distinct()
        return queryset_list

class AddressDetailAPIView(generics.RetrieveAPIView):
    queryset = models.Address.objects.all()
    serializer_class = serializers.AddressDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

class AddressCreateAPIView(generics.CreateAPIView):
    queryset = models.Address.objects.all()
    serializer_class = serializers.AddressCreateUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

class AddressUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = models.Address.objects.all()
    serializer_class = serializers.AddressCreateUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

class AddressDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = models.Address.objects.all()
    serializer_class = serializers.AddressDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

################################################################################

class BirthDateListAPIView(generics.ListAPIView):
    serializer_class = serializers.BirthDateListSerializer
    filter_backends= [filters.SearchFilter, filters.OrderingFilter]
    permission_classes = [permissions.IsAuthenticated]
    search_fields = ['year','month','day']
    pagination_class = pagination.DefaultPageNumberPagination #PageNumberPagination

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

class BirthDateDetailAPIView(generics.RetrieveAPIView):
    queryset = models.BirthDate.objects.all()
    serializer_class = serializers.BirthDateDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

class BirthDateCreateAPIView(generics.CreateAPIView):
    queryset = models.BirthDate.objects.all()
    serializer_class = serializers.BirthDateCreateUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

class BirthDateUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = models.BirthDate.objects.all()
    serializer_class = serializers.BirthDateCreateUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

class BirthDateDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = models.BirthDate.objects.all()
    serializer_class = serializers.BirthDateDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

################################################################################
