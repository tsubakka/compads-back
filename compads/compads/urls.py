from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from rest_framework_swagger.views import get_swagger_view

from compads.router import common_router as router

from api.urls import urlpatterns as api_urls
from api.clients.urls import urlpatterns as client_urls

schema_view = get_swagger_view(title='Compads API')

urlpatterns = [
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^api/', include(router.urls)),
    url(r'^api/docs/$', schema_view),

]

urlpatterns += api_urls
urlpatterns += client_urls
