from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    Serializer,
    CharField,
    ReadOnlyField,
    ListField,
    ChoiceField,
    RelatedField,
    StringRelatedField,
    HyperlinkedModelSerializer


)
from django.db.models import Count, Value

from django.core import serializers
import json

from rest_framework.response import Response

import api.clients.models as models

from api.utils import SerializerUrl



################################################################################

class ClientTypeListSerializer(ModelSerializer):
    detail_url = SerializerUrl.get_url('clients-api:client-type-detail')
    update_url = SerializerUrl.get_url('clients-api:client-type-update')
    delete_url = SerializerUrl.get_url('clients-api:client-type-delete')
    class Meta:
        model = models.ClientType
        fields = '__all__'

class ClientTypeCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = models.ClientType
        fields = '__all__'

class ClientTypeDetailSerializer(ModelSerializer):
    detail_url = SerializerUrl.get_url('clients-api:client-type-detail')
    update_url = SerializerUrl.get_url('clients-api:client-type-update')
    delete_url = SerializerUrl.get_url('clients-api:client-type-delete')
    class Meta:
        model = models.ClientType
        fields = '__all__'

################################################################################

class EmailListSerializer(ModelSerializer):
    detail_url = SerializerUrl.get_url('clients-api:email-detail')
    update_url = SerializerUrl.get_url('clients-api:email-update')
    delete_url = SerializerUrl.get_url('clients-api:email-delete')
    email_type_text = ReadOnlyField(source='email_type.email_type')
    client_name = ReadOnlyField(source='client.client_name')
    class Meta:
        model = models.Email
        fields = '__all__'

class EmailDetailSerializer(ModelSerializer):
    detail_url = SerializerUrl.get_url('clients-api:email-detail')
    update_url = SerializerUrl.get_url('clients-api:email-update')
    delete_url = SerializerUrl.get_url('clients-api:email-delete')
    email_type_text = ReadOnlyField(source='email_type.email_type')
    client_name = ReadOnlyField(source='client.client_name')
    class Meta:
        model = models.Email
        fields = '__all__'

class EmailCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = models.Email
        fields = '__all__'

################################################################################

class EmailTypeListSerializer(ModelSerializer):
    detail_url = SerializerUrl.get_url('clients-api:email-type-detail')
    update_url = SerializerUrl.get_url('clients-api:email-type-update')
    delete_url = SerializerUrl.get_url('clients-api:email-type-delete')
    class Meta:
        model = models.EmailType
        fields = '__all__'

class EmailTypeDetailSerializer(ModelSerializer):
    detail_url = SerializerUrl.get_url('clients-api:email-type-detail')
    update_url = SerializerUrl.get_url('clients-api:email-type-update')
    delete_url = SerializerUrl.get_url('clients-api:email-type-delete')
    class Meta:
        model = models.EmailType
        fields = '__all__'

class EmailTypeCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = models.EmailType
        fields = '__all__'

################################################################################

class PhoneListSerializer(ModelSerializer):
    detail_url = SerializerUrl.get_url('clients-api:phone-detail')
    update_url = SerializerUrl.get_url('clients-api:phone-update')
    delete_url = SerializerUrl.get_url('clients-api:phone-delete')
    phone_type_text = ReadOnlyField(source='phone_type.phone_type')
    client_name = ReadOnlyField(source='client.client_name')
    class Meta:
        model = models.Phone
        fields = '__all__'

class PhoneDetailSerializer(ModelSerializer):
    detail_url = SerializerUrl.get_url('clients-api:phone-detail')
    update_url = SerializerUrl.get_url('clients-api:phone-update')
    delete_url = SerializerUrl.get_url('clients-api:phone-delete')
    phone_type_text = ReadOnlyField(source='phone_type.phone_type')
    client_name = ReadOnlyField(source='client.client_name')
    class Meta:
        model = models.Phone
        fields = '__all__'

class PhoneCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = models.Phone
        fields = '__all__'

################################################################################

class PhoneTypeListSerializer(ModelSerializer):
    detail_url = SerializerUrl.get_url('clients-api:phone-type-detail')
    update_url = SerializerUrl.get_url('clients-api:phone-type-update')
    delete_url = SerializerUrl.get_url('clients-api:phone-type-delete')
    class Meta:
        model = models.PhoneType
        fields = '__all__'

class PhoneTypeDetailSerializer(ModelSerializer):
    detail_url = SerializerUrl.get_url('clients-api:phone-type-detail')
    update_url = SerializerUrl.get_url('clients-api:phone-type-update')
    delete_url = SerializerUrl.get_url('clients-api:phone-type-delete')
    class Meta:
        model = models.PhoneType
        fields = '__all__'

class PhoneTypeCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = models.PhoneType
        fields = '__all__'

################################################################################

class AddressListSerializer(ModelSerializer):
    detail_url = SerializerUrl.get_url('clients-api:address-detail')
    update_url = SerializerUrl.get_url('clients-api:address-update')
    delete_url = SerializerUrl.get_url('clients-api:address-delete')
    address_type_text = ReadOnlyField(source='address_type.address_type')
    client_name = ReadOnlyField(source='client.client_name')
    class Meta:
        model = models.Address
        fields = '__all__'

class AddressDetailSerializer(ModelSerializer):
    detail_url = SerializerUrl.get_url('clients-api:address-detail')
    update_url = SerializerUrl.get_url('clients-api:address-update')
    delete_url = SerializerUrl.get_url('clients-api:address-delete')
    address_type_text = ReadOnlyField(source='address_type.address_type')
    client_name = ReadOnlyField(source='client.client_name')
    class Meta:
        model = models.Address
        fields = '__all__'

class AddressCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = models.Address
        fields = '__all__'

################################################################################

class AddressTypeListSerializer(ModelSerializer):
    detail_url = SerializerUrl.get_url('clients-api:address-type-detail')
    update_url = SerializerUrl.get_url('clients-api:address-type-update')
    delete_url = SerializerUrl.get_url('clients-api:address-type-delete')
    class Meta:
        model = models.AddressType
        fields = '__all__'

class AddressTypeDetailSerializer(ModelSerializer):
    detail_url = SerializerUrl.get_url('clients-api:address-type-detail')
    update_url = SerializerUrl.get_url('clients-api:address-type-update')
    delete_url = SerializerUrl.get_url('clients-api:address-type-delete')
    class Meta:
        model = models.AddressType
        fields = '__all__'

class AddressTypeCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = models.AddressType
        fields = '__all__'

################################################################################

class BirthDateListSerializer(ModelSerializer):
    detail_url = SerializerUrl.get_url('clients-api:birthdate-detail')
    update_url = SerializerUrl.get_url('clients-api:birthdate-update')
    delete_url = SerializerUrl.get_url('clients-api:birthdate-delete')
    class Meta:
        model = models.BirthDate
        fields = '__all__'

class BirthDateDetailSerializer(ModelSerializer):
    detail_url = SerializerUrl.get_url('clients-api:birthdate-detail')
    update_url = SerializerUrl.get_url('clients-api:birthdate-update')
    delete_url = SerializerUrl.get_url('clients-api:birthdate-delete')
    class Meta:
        model = models.BirthDate
        fields = '__all__'

class BirthDateCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = models.BirthDate
        fields = '__all__'

################################################################################

class ClientListSerializer(ModelSerializer):
    detail_url = SerializerUrl.get_url('clients-api:client-detail')
    update_url = SerializerUrl.get_url('clients-api:client-update')
    delete_url = SerializerUrl.get_url('clients-api:client-delete')
    emails_url = SerializerUrl.get_url('clients-api:client-emails')
    phones_url = SerializerUrl.get_url('clients-api:client-phones')
    addresses_url = SerializerUrl.get_url('clients-api:client-addresses')
    birthdate_url = SerializerUrl.get_url('clients-api:client-birthdate')
    client_emails =  EmailListSerializer(many=True, read_only=True)
    client_phones =  PhoneListSerializer(many=True, read_only=True)
    client_addresses =  AddressListSerializer(many=True, read_only=True)
    client_birthdate =  BirthDateListSerializer(read_only=True)
    client_type_text = ReadOnlyField(source='client_type.client_type')
    class Meta:
        model = models.Client
        fields = '__all__'

class ClientDetailSerializer(ModelSerializer):

    detail_url = SerializerUrl.get_url('clients-api:client-detail')
    update_url = SerializerUrl.get_url('clients-api:client-update')
    delete_url = SerializerUrl.get_url('clients-api:client-delete')
    emails_url = SerializerUrl.get_url('clients-api:client-emails')
    phones_url = SerializerUrl.get_url('clients-api:client-phones')
    addresses_url = SerializerUrl.get_url('clients-api:client-addresses')
    birthdate_url = SerializerUrl.get_url('clients-api:client-birthdate')
    client_emails =  EmailListSerializer(many=True, read_only=True)
    client_phones =  PhoneListSerializer(many=True, read_only=True)
    client_addresses =  AddressListSerializer(many=True, read_only=True)
    client_birthdate =  BirthDateListSerializer(read_only=True)
    client_type_text = ReadOnlyField(source='client_type.client_type')
    class Meta:
        model = models.Client
        fields = '__all__'

class ClientCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = models.Client
        fields = '__all__'

################################################################################
