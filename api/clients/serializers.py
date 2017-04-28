import rest_framework.serializers as serializers
from rest_framework.response import Response
import api.clients.models as models
from api.utils import SerializerUrl

################################################################################

class EmailSerializer(serializers.ModelSerializer):
    url = SerializerUrl.get_url('email-detail')
    email_type_text = serializers.ReadOnlyField(source='email_type.email_type')
    client_name = serializers.ReadOnlyField(source='client.client_name')
    class Meta:
        model = models.Email
        fields = '__all__'

################################################################################

class EmailTypeSerializer(serializers.ModelSerializer):
    url = SerializerUrl.get_url('email-type-detail')
    class Meta:
        model = models.EmailType
        fields = '__all__'

################################################################################

class PhoneSerializer(serializers.ModelSerializer):
    url = SerializerUrl.get_url('phone-detail')
    phone_type_text = serializers.ReadOnlyField(source='phone_type.phone_type')
    client_name = serializers.ReadOnlyField(source='client.client_name')
    class Meta:
        model = models.Phone
        fields = '__all__'

################################################################################

class PhoneTypeSerializer(serializers.ModelSerializer):
    url = SerializerUrl.get_url('phone-type-detail')
    class Meta:
        model = models.PhoneType
        fields = '__all__'

################################################################################

class AddressSerializer(serializers.ModelSerializer):
    detail_url = SerializerUrl.get_url('address-detail')
    address_type_text = serializers.ReadOnlyField(source='address_type.address_type')
    client_name = serializers.ReadOnlyField(source='client.client_name')
    class Meta:
        model = models.Address
        fields = '__all__'

################################################################################

class AddressTypeSerializer(serializers.ModelSerializer):
    url = SerializerUrl.get_url('address-type-detail')
    class Meta:
        model = models.AddressType
        fields = '__all__'

################################################################################

class BirthDateSerializer(serializers.ModelSerializer):
    url = SerializerUrl.get_url('birthdate-detail')
    class Meta:
        model = models.BirthDate
        fields = '__all__'

################################################################################

class ClientTypeSerializer(serializers.ModelSerializer):
    url = SerializerUrl.get_url('client-type-detail')
    class Meta:
        model = models.ClientType
        fields = '__all__'

################################################################################

class ClientListModeModelSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        # Instantiate the superclass normally
        super(ClientListModeModelSerializer, self).__init__(*args, **kwargs)

        listmode = self.context['request'].query_params.get('listmode')
        if not listmode:
            listmode = 'details'
        if listmode:
            if listmode=='urls':
                disallowed = set(['client_emails', 'client_phones', 'client_addresses', 'client_birthdate'])
                existing = set(self.fields.keys())
                for field_name in existing: # - allowed:
                    if field_name in disallowed:
                        self.fields.pop(field_name)

            if listmode=='details':
                disallowed = set(['emails_url', 'phones_url', 'addresses_url', 'birthdate_url'])
                existing = set(self.fields.keys())
                for field_name in existing: # - allowed:
                    if field_name in disallowed:
                        self.fields.pop(field_name)

            if listmode=='full':
                disallowed = set([])
                existing = set(self.fields.keys())
                for field_name in existing: # - allowed:
                    if field_name in disallowed:
                        self.fields.pop(field_name)

################################################################################

class ClientSerializer(ClientListModeModelSerializer):
    url = SerializerUrl.get_url('client-detail')
    emails_url = SerializerUrl.get_url('client-emails')
    phones_url = SerializerUrl.get_url('client-phones')
    addresses_url = SerializerUrl.get_url('client-addresses')
    birthdate_url = SerializerUrl.get_url('client-birthdate')
    client_emails =  EmailSerializer(many=True, read_only=True)
    client_phones =  PhoneSerializer(many=True, read_only=True)
    client_addresses =  AddressSerializer(many=True, read_only=True)
    #client_birthdate =  BirthDateSerializer(read_only=True)
    client_type_text = serializers.ReadOnlyField(source='client_type.client_type')

    class Meta:
        model = models.Client
        fields = '__all__'

################################################################################
