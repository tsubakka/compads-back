from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from rest_framework_jwt.views import obtain_jwt_token

from api.views import api_root

from api.urls import urlpatterns as api_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/$', api_root),
]
urlpatterns += api_urls
