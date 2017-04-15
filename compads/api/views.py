from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
import json

@api_view(['GET'])
def api_root(request, format=None):

    router = {
        'auth-token': reverse('auth-token', request=request, format=format),
#####
        'user-login': reverse('users-api:user-login', request=request, format=format),
        'user-create': reverse('users-api:user-create', request=request, format=format),

        'client-list': reverse('clients-api:client-list', request=request, format=format),
        'client-create': reverse('clients-api:client-create', request=request, format=format),
        'client-type-list': reverse('clients-api:client-type-list', request=request, format=format),
        'client-type-create': reverse('clients-api:client-type-create', request=request, format=format),

        'phone-list': reverse('clients-api:phone-list', request=request, format=format),
        'phone-create': reverse('clients-api:phone-create', request=request, format=format),
        'phone-type-list': reverse('clients-api:phone-type-list', request=request, format=format),
        'phone-type-create': reverse('clients-api:phone-type-create', request=request, format=format),

        'email-list': reverse('clients-api:email-list', request=request, format=format),
        'email-create': reverse('clients-api:email-create', request=request, format=format),
        'email-type-list': reverse('clients-api:email-type-list', request=request, format=format),
        'email-type-create': reverse('clients-api:email-type-create', request=request, format=format),

        'address-list': reverse('clients-api:address-list', request=request, format=format),
        'address-create': reverse('clients-api:address-create', request=request, format=format),
        'address-type-list': reverse('clients-api:address-type-list', request=request, format=format),
        'address-type-create': reverse('clients-api:address-type-create', request=request, format=format),

        'birthdate-list': reverse('clients-api:birthdate-list', request=request, format=format),
        'birthdate-create': reverse('clients-api:birthdate-create', request=request, format=format),

    }

    return Response(router)
