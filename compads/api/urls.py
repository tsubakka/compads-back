from rest_framework_jwt.views import obtain_jwt_token
from django.conf.urls import include, url
#from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = ([
    url(r'^api/auth/token/', obtain_jwt_token, name='auth-token'),
    url(r'^api/users/', include("api.accounts.urls", namespace='users-api'),name="users"),#, namespace='users-api')),
    url(r'^api/clients/', include("api.clients.urls", namespace='clients-api'),name="clients"),
])
