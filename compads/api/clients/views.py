from django.db.models import Q

from rest_framework.response import Response

from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    ListCreateAPIView,
    RetrieveDestroyAPIView
)

from .pagination import (
    ClientTypeLimitOffsetPagination,
    ClientTypePageNumberPagination,
    DefaultLimitOffsetPagination,
    DefaultPageNumberPagination,
)

from .permissions import IsOwnerOrReadOnly

from .serializers import (
    ClientTypeListSerializer,
    ClientTypeCreateUpdateSerializer,
    ClientTypeDetailSerializer,
    ClientListSerializer,
    ClientCreateUpdateSerializer,
    ClientDetailSerializer,
    EmailTypeListSerializer,
    EmailTypeCreateUpdateSerializer,
    EmailTypeDetailSerializer,
    EmailListSerializer,
    EmailCreateUpdateSerializer,
    EmailDetailSerializer,
    PhoneTypeListSerializer,
    PhoneTypeCreateUpdateSerializer,
    PhoneTypeDetailSerializer,
    PhoneListSerializer,
    PhoneCreateUpdateSerializer,
    PhoneDetailSerializer,
    AddressTypeListSerializer,
    AddressTypeCreateUpdateSerializer,
    AddressTypeDetailSerializer,
    AddressListSerializer,
    AddressCreateUpdateSerializer,
    AddressDetailSerializer,
)

import api.clients.serializers as serializers

from .models import (
    ClientType,
    Client,
    EmailType,
    Email,
    Address,
    AddressType,
    Phone,
    PhoneType
)

import api.clients.models as models

################################################################################

class ClientTypeListAPIView(ListAPIView):
    serializer_class = ClientTypeListSerializer
    filter_backends= [SearchFilter, OrderingFilter]
    permission_classes = [IsAuthenticated]
    search_fields = ['client_type',]
    pagination_class = DefaultPageNumberPagination #PageNumberPagination
    def get_queryset(self, *args, **kwargs):
        #queryset_list = super(PostListAPIView, self).get_queryset(*args, **kwargs)
        queryset_list = ClientType.objects.all() #filter(user=self.request.user)
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                    Q(client_type__icontains=query)#|
                #    Q(content__icontains=query)|
                #    Q(user__first_name__icontains=query) |
                #    Q(user__last_name__icontains=query)
                    ).distinct()
        return queryset_list

class ClientTypeCreateAPIView(CreateAPIView):
    queryset = ClientType.objects.all()
    serializer_class = ClientTypeCreateUpdateSerializer
    permission_classes = [IsAuthenticated]
    #def perform_create(self, serializer):
    #    serializer.save(user=self.request.user)

class ClientTypeDetailAPIView(RetrieveAPIView):
    queryset = ClientType.objects.all()
    serializer_class = ClientTypeDetailSerializer
    permission_classes = [IsAuthenticated]

class ClientTypeUpdateAPIView(RetrieveUpdateAPIView):
    queryset = ClientType.objects.all()
    serializer_class = ClientTypeCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

class ClientTypeDeleteAPIView(RetrieveDestroyAPIView):
    queryset = ClientType.objects.all()
    serializer_class = ClientTypeDetailSerializer
    permission_classes = [IsAuthenticated]

################################################################################

class ClientListAPIView(ListAPIView):
    serializer_class = ClientListSerializer
    filter_backends= [SearchFilter, OrderingFilter]
    permission_classes = [IsAuthenticated]
    search_fields = ['first_name','last_name','company_name']
    pagination_class = DefaultPageNumberPagination #PageNumberPagination

    def get_queryset(self, *args, **kwargs):
        #queryset_list = super(PostListAPIView, self).get_queryset(*args, **kwargs)
        queryset_list = Client.objects.all() #filter(user=self.request.user)
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                    Q(client_type__icontains=query)#|
                #    Q(content__icontains=query)|
                #    Q(user__first_name__icontains=query) |
                #    Q(user__last_name__icontains=query)
                    ).distinct()
        return queryset_list

class ClientDetailAPIView(RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientDetailSerializer
    permission_classes = [IsAuthenticated]

class ClientCreateAPIView(CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

class ClientUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

class ClientDeleteAPIView(RetrieveDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientDetailSerializer
    permission_classes = [IsAuthenticated]

class ClientEmailListAPIView(ListAPIView):
    #queryset = models.Email.objects.all()
    serializer_class = serializers.EmailListSerializer
    permission_classes = [IsAuthenticated]
    #lookup_field='pk'
    def get_queryset(self):
        return models.Email.objects.filter(client_id=self.kwargs['pk'])

class ClientPhoneListAPIView(ListAPIView):
    #queryset = models.Phone.objects.all()
    serializer_class = serializers.PhoneListSerializer
    permission_classes = [IsAuthenticated]
    #lookup_field='pk'
    def get_queryset(self):
        return models.Phone.objects.filter(client_id=self.kwargs['pk'])

class ClientAddressListAPIView(ListAPIView):
    #queryset = models.Address.objects.all()
    serializer_class = serializers.AddressListSerializer
    permission_classes = [IsAuthenticated]
    #lookup_field='pk'
    def get_queryset(self):
        return models.Address.objects.filter(client_id=self.kwargs['pk'])

class ClientBirthDateAPIView(ListAPIView):
    #queryset = models.Address.objects.all()
    serializer_class = serializers.BirthDateListSerializer
    permission_classes = [IsAuthenticated]
    #lookup_field='pk'
    def get_queryset(self):
        return models.BirthDate.objects.filter(client_id=self.kwargs['pk'])

################################################################################

class PhoneListAPIView(ListAPIView):
    serializer_class = PhoneListSerializer
    filter_backends= [SearchFilter, OrderingFilter]
    permission_classes = [IsAuthenticated]
    search_fields = ['first_name','last_name','company_name']
    pagination_class = DefaultPageNumberPagination #PageNumberPagination
    def get_queryset(self, *args, **kwargs):
        #queryset_list = super(PostListAPIView, self).get_queryset(*args, **kwargs)
        queryset_list = Phone.objects.all() #filter(user=self.request.user)
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                    Q(client_type__icontains=query)#|
                #    Q(content__icontains=query)|
                #    Q(user__first_name__icontains=query) |
                #    Q(user__last_name__icontains=query)
                    ).distinct()
        return queryset_list

class PhoneDetailAPIView(RetrieveAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneDetailSerializer
    permission_classes = [IsAuthenticated]

class PhoneCreateAPIView(CreateAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

class PhoneUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

class PhoneDeleteAPIView(RetrieveDestroyAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneDetailSerializer
    permission_classes = [IsAuthenticated]

################################################################################

class PhoneTypeListAPIView(ListAPIView):
    serializer_class = PhoneTypeListSerializer
    filter_backends= [SearchFilter, OrderingFilter]
    permission_classes = [IsAuthenticated]
    search_fields = ['first_name','last_name','company_name']
    pagination_class = DefaultPageNumberPagination #PageNumberPagination

    def get_queryset(self, *args, **kwargs):
        #queryset_list = super(PostListAPIView, self).get_queryset(*args, **kwargs)
        queryset_list = PhoneType.objects.all() #filter(user=self.request.user)
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                    Q(client_type__icontains=query)#|
                #    Q(content__icontains=query)|
                #    Q(user__first_name__icontains=query) |
                #    Q(user__last_name__icontains=query)
                    ).distinct()
        return queryset_list

class PhoneTypeDetailAPIView(RetrieveAPIView):
    queryset = PhoneType.objects.all()
    serializer_class = PhoneTypeDetailSerializer
    permission_classes = [IsAuthenticated]

class PhoneTypeCreateAPIView(CreateAPIView):
    queryset = PhoneType.objects.all()
    serializer_class = PhoneTypeCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

class PhoneTypeUpdateAPIView(RetrieveUpdateAPIView):
    queryset = PhoneType.objects.all()
    serializer_class = PhoneTypeCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

class PhoneTypeDeleteAPIView(RetrieveDestroyAPIView):
    queryset = PhoneType.objects.all()
    serializer_class = PhoneTypeDetailSerializer
    permission_classes = [IsAuthenticated]

################################################################################

class EmailListAPIView(ListAPIView):
    serializer_class = EmailListSerializer
    filter_backends= [SearchFilter, OrderingFilter]
    permission_classes = [IsAuthenticated]
    search_fields = ['email_address']
    pagination_class = DefaultPageNumberPagination #PageNumberPagination

    def get_queryset(self, *args, **kwargs):
        #queryset_list = super(PostListAPIView, self).get_queryset(*args, **kwargs)
        queryset_list = Email.objects.all() #filter(user=self.request.user)
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                    Q(client_type__icontains=query)#|
                #    Q(content__icontains=query)|
                #    Q(user__first_name__icontains=query) |
                #    Q(user__last_name__icontains=query)
                    ).distinct()
        return queryset_list

class EmailDetailAPIView(RetrieveAPIView):
    queryset = Email.objects.all()
    serializer_class = EmailDetailSerializer
    permission_classes = [IsAuthenticated]

class EmailCreateAPIView(CreateAPIView):
    queryset = Email.objects.all()
    serializer_class = EmailCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

class EmailUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Email.objects.all()
    serializer_class = EmailCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

class EmailDeleteAPIView(RetrieveDestroyAPIView):
    queryset = Email.objects.all()
    serializer_class = EmailDetailSerializer
    permission_classes = [IsAuthenticated]

################################################################################

class EmailTypeListAPIView(ListAPIView):
    serializer_class = EmailTypeListSerializer
    filter_backends= [SearchFilter, OrderingFilter]
    permission_classes = [IsAuthenticated]
    search_fields = ['first_name','last_name','company_name']
    pagination_class = DefaultPageNumberPagination #PageNumberPagination

    def get_queryset(self, *args, **kwargs):
        #queryset_list = super(PostListAPIView, self).get_queryset(*args, **kwargs)
        queryset_list = EmailType.objects.all() #filter(user=self.request.user)
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                    Q(client_type__icontains=query)#|
                #    Q(content__icontains=query)|
                #    Q(user__first_name__icontains=query) |
                #    Q(user__last_name__icontains=query)
                    ).distinct()
        return queryset_list

class EmailTypeDetailAPIView(RetrieveAPIView):
    queryset = EmailType.objects.all()
    serializer_class = EmailTypeDetailSerializer
    permission_classes = [IsAuthenticated]

class EmailTypeCreateAPIView(CreateAPIView):
    queryset = EmailType.objects.all()
    serializer_class = EmailTypeCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

class EmailTypeUpdateAPIView(RetrieveUpdateAPIView):
    queryset = EmailType.objects.all()
    serializer_class = EmailTypeCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

class EmailTypeDeleteAPIView(RetrieveDestroyAPIView):
    queryset = EmailType.objects.all()
    serializer_class = EmailTypeDetailSerializer
    permission_classes = [IsAuthenticated]

################################################################################

class AddressTypeListAPIView(ListAPIView):
    serializer_class = AddressTypeListSerializer
    filter_backends= [SearchFilter, OrderingFilter]
    permission_classes = [IsAuthenticated]
    search_fields = ['first_name','last_name','company_name']
    pagination_class = DefaultPageNumberPagination #PageNumberPagination

    def get_queryset(self, *args, **kwargs):
        #queryset_list = super(PostListAPIView, self).get_queryset(*args, **kwargs)
        queryset_list = AddressType.objects.all() #filter(user=self.request.user)
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                    Q(AddressType_type__icontains=query)#|
                #    Q(content__icontains=query)|
                #    Q(user__first_name__icontains=query) |
                #    Q(user__last_name__icontains=query)
                    ).distinct()
        return queryset_list

class AddressTypeDetailAPIView(RetrieveAPIView):
    queryset = AddressType.objects.all()
    serializer_class = AddressTypeDetailSerializer
    permission_classes = [IsAuthenticated]

class AddressTypeCreateAPIView(CreateAPIView):
    queryset = AddressType.objects.all()
    serializer_class = AddressTypeCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

class AddressTypeUpdateAPIView(RetrieveUpdateAPIView):
    queryset = AddressType.objects.all()
    serializer_class = AddressTypeCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

class AddressTypeDeleteAPIView(RetrieveDestroyAPIView):
    queryset = AddressType.objects.all()
    serializer_class = AddressTypeDetailSerializer
    permission_classes = [IsAuthenticated]

################################################################################

class AddressListAPIView(ListAPIView):
    serializer_class = AddressListSerializer
    filter_backends= [SearchFilter, OrderingFilter]
    permission_classes = [IsAuthenticated]
    search_fields = ['first_name','last_name','company_name']
    pagination_class = DefaultPageNumberPagination #PageNumberPagination

    def get_queryset(self, *args, **kwargs):
        #queryset_list = super(PostListAPIView, self).get_queryset(*args, **kwargs)
        queryset_list = Address.objects.all() #filter(user=self.request.user)
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                    Q(Address_type__icontains=query)#|
                #    Q(content__icontains=query)|
                #    Q(user__first_name__icontains=query) |
                #    Q(user__last_name__icontains=query)
                    ).distinct()
        return queryset_list

class AddressDetailAPIView(RetrieveAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressDetailSerializer
    permission_classes = [IsAuthenticated]

class AddressCreateAPIView(CreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

class AddressUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

class AddressDeleteAPIView(RetrieveDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressDetailSerializer
    permission_classes = [IsAuthenticated]

################################################################################

class BirthDateListAPIView(ListAPIView):
    serializer_class = serializers.BirthDateListSerializer
    filter_backends= [SearchFilter, OrderingFilter]
    permission_classes = [IsAuthenticated]
    search_fields = ['year','month','day']
    pagination_class = DefaultPageNumberPagination #PageNumberPagination

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

class BirthDateDetailAPIView(RetrieveAPIView):
    queryset = models.BirthDate.objects.all()
    serializer_class = serializers.BirthDateDetailSerializer
    permission_classes = [IsAuthenticated]

class BirthDateCreateAPIView(CreateAPIView):
    queryset = models.BirthDate.objects.all()
    serializer_class = serializers.BirthDateCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

class BirthDateUpdateAPIView(RetrieveUpdateAPIView):
    queryset = models.BirthDate.objects.all()
    serializer_class = serializers.BirthDateCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

class BirthDateDeleteAPIView(RetrieveDestroyAPIView):
    queryset = models.BirthDate.objects.all()
    serializer_class = serializers.BirthDateDetailSerializer
    permission_classes = [IsAuthenticated]

################################################################################
