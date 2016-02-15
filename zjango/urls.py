from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^api/', include('datacollection.urls')),
    url(r'^postgres/', include('postgres.urls')),
    url(r'^admin/', admin.site.urls),
]