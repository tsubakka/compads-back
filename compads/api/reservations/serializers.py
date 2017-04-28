import rest_framework.serializers as serializers
from rest_framework.response import Response
import api.reservations.models as models
from django.contrib.auth.models import User
import api.clients.models as clientModels
from api.utils import SerializerUrl
import json
from django.core.serializers import serialize

################################################################################

class SzallasJellegSerializer(serializers.ModelSerializer):
    #url = SerializerUrl.get_url('email-detail')
    #email_type_text = serializers.ReadOnlyField(source='email_type.email_type')
    #client_name = serializers.ReadOnlyField(source='client.client_name')
    class Meta:
        model = models.SzallasJelleg
        fields = '__all__'

################################################################################

class SzallasTipusSerializer(serializers.ModelSerializer):
    url = SerializerUrl.get_url('szallas-tipus-detail')
    #email_type_text = serializers.ReadOnlyField(source='email_type.email_type')
    #client_name = serializers.ReadOnlyField(source='client.client_name')
    class Meta:
        model = models.SzallasTipus
        fields = '__all__'

################################################################################

class SzallasReszTipusSerializer(serializers.ModelSerializer):
    url = SerializerUrl.get_url('szallasresz-tipus-detail')
    #email_type_text = serializers.ReadOnlyField(source='email_type.email_type')
    #client_name = serializers.ReadOnlyField(source='client.client_name')
    class Meta:
        model = models.SzallasReszTipus
        fields = '__all__'

################################################################################

class SzallasReszSerializer(serializers.ModelSerializer):
    url = SerializerUrl.get_url('szallasresz-detail')
    szallasresz_tipus_text = serializers.ReadOnlyField(source='szallasresz_tipus.szallasresz_tipus')
    szallas_text = serializers.ReadOnlyField(source='szallas.szallas_nev')
    #client_name = serializers.ReadOnlyField(source='client.client_name')
    class Meta:
        model = models.SzallasResz
        fields = '__all__'

################################################################################

class AgyTipusSerializer(serializers.ModelSerializer):
    url = SerializerUrl.get_url('agy-tipus-detail')
    #email_type_text = serializers.ReadOnlyField(source='email_type.email_type')
    #client_name = serializers.ReadOnlyField(source='client.client_name')
    class Meta:
        model = models.AgyTipus
        fields = '__all__'

################################################################################

class AlapArSerializer(serializers.ModelSerializer):
    url = SerializerUrl.get_url('alap-ar-detail')
    szallas_tipus_text = serializers.ReadOnlyField(source='szallas_tipus.szallas_tipus')
    agy_tipus_text = serializers.ReadOnlyField(source='agy_tipus.agy_tipus')
    class Meta:
        model = models.AlapAr
        fields = '__all__'

################################################################################

class SzallasListModeModelSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        # Instantiate the superclass normally
        super(SzallasListModeModelSerializer, self).__init__(*args, **kwargs)

        listmode = self.context['request'].query_params.get('listmode')
        if not listmode:
            listmode = 'details'
        if listmode:
            if listmode=='urls':
                disallowed = set(['szallas_szallasreszek'])
                existing = set(self.fields.keys())
                for field_name in existing: # - allowed:
                    if field_name in disallowed:
                        self.fields.pop(field_name)

            if listmode=='details':
                disallowed = set(['szallasreszek_url'])
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

class SzallasSerializer(SzallasListModeModelSerializer):
    url = SerializerUrl.get_url('szallas-detail')
    szallasreszek_url = SerializerUrl.get_url('szallas-szallasresz-list')
    szallas_tipus_text = serializers.ReadOnlyField(source='szallas_tipus.szallas_tipus')
    szallas_jelleg_text = serializers.ReadOnlyField(source='szallas_jelleg.szallas_jelleg')
    szallas_szallasreszek = SzallasReszSerializer(many=True, read_only=True)

    class Meta:
        model = models.Szallas
        fields = '__all__'

################################################################################


class AjanlatReszSerializer(serializers.ModelSerializer):
    url = SerializerUrl.get_url('ajanlatresz-detail')
    sajanlat_text = serializers.ReadOnlyField(source='ajanlat.__unicode__')
    szallasresz_text = serializers.ReadOnlyField(source='szallasresz.__unicode__')

    class Meta:
        model = models.AjanlatResz
        fields = '__all__'

################################################################################


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = clientModels.Client
        fields = ('id','nev','url')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','first_name','last_name','email')


class AjanlatSerializer(serializers.ModelSerializer):
    url = SerializerUrl.get_url('ajanlat-detail')
    ajanlatreszek_url = SerializerUrl.get_url('ajanlat-ajanlatresz-list')
    ugyfel = ClientSerializer(read_only=True, many=False)
    ajanlatado = UserSerializer(read_only=True, many=False)
    ajanlat_ajanlatreszek = AjanlatReszSerializer(many=True, read_only=True)
    ajanlatado_text = serializers.ReadOnlyField(source='user_')
    #szallas_szallasreszek = SzallasReszSerializer(many=True, read_only=True)

    class Meta:
        model = models.Ajanlat
        fields = '__all__'

"""    def ugyfel_nev(self, obj):
        ugyfel = clientModels.Client.objects.filter(id=str(obj.ugyfel_id))
        #ugyfel_data = serializers.serialize('json', list(ugyfel), fields=('first_name')
        ugyfel_data = (serialize('json',ugyfel))
        ugyfelnev = ugyfel_data
        #if (ugyfel['client_type_id'] == '2'):
        #    ugyfelnev = ugyfel['company_name']
        return ugyfelnev
"""

################################################################################












































################################################################################
