from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from rest_framework_jwt.views import obtain_jwt_token

from api.views import api_root

from api.urls import urlpatterns as api_urls
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Compads API')


urlpatterns = [
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^api/$', api_root, name='api'),
    url(r'^api/docs/$', schema_view),

]
urlpatterns += api_urls
