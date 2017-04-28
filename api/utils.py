from rest_framework.serializers import (
    HyperlinkedIdentityField,
)

class SerializerUrl():
    def get_url (view_name, *lookup_field):
        return HyperlinkedIdentityField(view_name=view_name,lookup_field='pk')
