from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^', include('mcoauth.core.urls')),
    url(r'^accounts/', include('mcoauth.accounts.urls')),
    url(r'^oauth2/', include('provider.oauth2.urls', namespace='oauth2')),
    url(r'^admin/', include(admin.site.urls)),
)