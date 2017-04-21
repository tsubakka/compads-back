import  rest_framework.serializers as serializers

from rest_framework.response import Response

import api.clients.models as models

from api.utils import SerializerUrl

################################################################################

class ClientTypeListSerializer(serializers.ModelSerializer):
    detail_url = SerializerUrl.get_url('clients-api:client-type-detail')
    update_url = SerializerUrl.get_url('clients-api:client-type-update')
    delete_url = SerializerUrl.get_url('clients-api:client-type-delete')
    class Meta:
        model = models.ClientType
        fields = '__all__'

class ClientTypeCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ClientType
        fields = '__all__'

class ClientTypeDetailSerializer(serializers.ModelSerializer):
    detail_url = SerializerUrl.get_url('clients-api:client-type-detail')
    update_url = SerializerUrl.get_url('clients-api:client-type-update')
    delete_url = SerializerUrl.get_url('clients-api:client-type-delete')
    class Meta:
        model = models.ClientType
        fields = '__all__'

################################################################################

class EmailListSerializer(serializers.ModelSerializer):
    detail_url = SerializerUrl.get_url('clients-api:email-detail')
    update_url = SerializerUrl.get_url('clients-api:email-update')
    delete_url = SerializerUrl.get_url('clients-api:email-delete')
    email_type_text = serializers.ReadOnlyField(source='email_type.email_type')
    client_name = serializers.ReadOnlyField(source='client.client_name')
    class Meta:
        model = models.Email
        fields = '__all__'

class EmailDetailSerializer(serializers.ModelSerializer):
    detail_url = SerializerUrl.get_url('clients-api:email-detail')
    update_url = SerializerUrl.get_url('clients-api:email-update')
    delete_url = SerializerUrl.get_url('clients-api:email-delete')
    email_type_text = serializers.ReadOnlyField(source='email_type.email_type')
    client_name = serializers.ReadOnlyField(source='client.client_name')
    class Meta:
        model = models.Email
        fields = '__all__'

class EmailCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Email
        fields = '__all__'

################################################################################

class EmailTypeListSerializer(serializers.ModelSerializer):
    detail_url = SerializerUrl.get_url('clients-api:email-type-detail')
    update_url = SerializerUrl.get_url('clients-api:email-type-update')
    delete_url = SerializerUrl.get_url('clients-api:email-type-delete')
    class Meta:
        model = models.EmailType
        fields = '__all__'

class EmailTypeDetailSerializer(serializers.ModelSerializer):
    detail_url = SerializerUrl.get_url('clients-api:email-type-detail')
    update_url = SerializerUrl.get_url('clients-api:email-type-update')
    delete_url = SerializerUrl.get_url('clients-api:email-type-delete')
    class Meta:
        model = models.EmailType
        fields = '__all__'

class EmailTypeCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EmailType
        fields = '__all__'

################################################################################

class PhoneListSerializer(serializers.ModelSerializer):
    detail_url = SerializerUrl.get_url('clients-api:phone-detail')
    update_url = SerializerUrl.get_url('clients-api:phone-update')
    delete_url = SerializerUrl.get_url('clients-api:phone-delete')
    phone_type_text = serializers.ReadOnlyField(source='phone_type.phone_type')
    client_name = serializers.ReadOnlyField(source='client.client_name')
    class Meta:
        model = models.Phone
        fields = '__all__'

class PhoneDetailSerializer(serializers.ModelSerializer):
    detail_url = SerializerUrl.get_url('clients-api:phone-detail')
    update_url = SerializerUrl.get_url('clients-api:phone-update')
    delete_url = SerializerUrl.get_url('clients-api:phone-delete')
    phone_type_text = serializers.ReadOnlyField(source='phone_type.phone_type')
    client_name = serializers.ReadOnlyField(source='client.client_name')
    class Meta:
        model = models.Phone
        fields = '__all__'

class PhoneCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Phone
        fields = '__all__'

################################################################################

class PhoneTypeListSerializer(serializers.ModelSerializer):
    detail_url = SerializerUrl.get_url('clients-api:phone-type-detail')
    update_url = SerializerUrl.get_url('clients-api:phone-type-update')
    delete_url = SerializerUrl.get_url('clients-api:phone-type-delete')
    class Meta:
        model = models.PhoneType
        fields = '__all__'

class PhoneTypeDetailSerializer(serializers.ModelSerializer):
    detail_url = SerializerUrl.get_url('clients-api:phone-type-detail')
    update_url = SerializerUrl.get_url('clients-api:phone-type-update')
    delete_url = SerializerUrl.get_url('clients-api:phone-type-delete')
    class Meta:
        model = models.PhoneType
        fields = '__all__'

class PhoneTypeCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PhoneType
        fields = '__all__'

################################################################################

class AddressListSerializer(serializers.ModelSerializer):
    detail_url = SerializerUrl.get_url('clients-api:address-detail')
    update_url = SerializerUrl.get_url('clients-api:address-update')
    delete_url = SerializerUrl.get_url('clients-api:address-delete')
    address_type_text = serializers.ReadOnlyField(source='address_type.address_type')
    client_name = serializers.ReadOnlyField(source='client.client_name')
    class Meta:
        model = models.Address
        fields = '__all__'

class AddressDetailSerializer(serializers.ModelSerializer):
    detail_url = SerializerUrl.get_url('clients-api:address-detail')
    update_url = SerializerUrl.get_url('clients-api:address-update')
    delete_url = SerializerUrl.get_url('clients-api:address-delete')
    address_type_text = serializers.ReadOnlyField(source='address_type.address_type')
    client_name = serializers.ReadOnlyField(source='client.client_name')
    class Meta:
        model = models.Address
        fields = '__all__'

class AddressCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Address
        fields = '__all__'

################################################################################

class AddressTypeListSerializer(serializers.ModelSerializer):
    detail_url = SerializerUrl.get_url('clients-api:address-type-detail')
    update_url = SerializerUrl.get_url('clients-api:address-type-update')
    delete_url = SerializerUrl.get_url('clients-api:address-type-delete')
    class Meta:
        model = models.AddressType
        fields = '__all__'

class AddressTypeDetailSerializer(serializers.ModelSerializer):
    detail_url = SerializerUrl.get_url('clients-api:address-type-detail')
    update_url = SerializerUrl.get_url('clients-api:address-type-update')
    delete_url = SerializerUrl.get_url('clients-api:address-type-delete')
    class Meta:
        model = models.AddressType
        fields = '__all__'

class AddressTypeCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AddressType
        fields = '__all__'

################################################################################

class BirthDateListSerializer(serializers.ModelSerializer):
    detail_url = SerializerUrl.get_url('clients-api:birthdate-detail')
    update_url = SerializerUrl.get_url('clients-api:birthdate-update')
    delete_url = SerializerUrl.get_url('clients-api:birthdate-delete')
    class Meta:
        model = models.BirthDate
        fields = '__all__'

class BirthDateDetailSerializer(serializers.ModelSerializer):
    detail_url = SerializerUrl.get_url('clients-api:birthdate-detail')
    update_url = SerializerUrl.get_url('clients-api:birthdate-update')
    delete_url = SerializerUrl.get_url('clients-api:birthdate-delete')
    class Meta:
        model = models.BirthDate
        fields = '__all__'

class BirthDateCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BirthDate
        fields = '__all__'

################################################################################

class ClientListSerializer(serializers.ModelSerializer):
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
    client_type_text = serializers.ReadOnlyField(source='client_type.client_type')
    #urls = SerializerMethodField('get_url_list')
    class Meta:
        model = models.Client
        fields = '__all__'
    #def get_url_list(self,request):
    #    url_list = {'1':"xxxxxxxxxxxxxxxxxx",'2':serializers.serialize(SerializerUrl.get_url('clients-api:client-birthdate'))}
    #    return url_list

class ClientDetailSerializer(serializers.ModelSerializer):

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
    client_type_text = serializers.ReadOnlyField(source='client_type.client_type')
    class Meta:
        model = models.Client
        fields = '__all__'

class ClientCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        fields = '__all__'

################################################################################
