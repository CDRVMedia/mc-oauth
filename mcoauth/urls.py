from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^', include('mcoauth.core.urls')),
    url(r'^accounts/', include('mcoauth.accounts.urls')),
    url(r'^apps/', include('mcoauth.apps.urls', namespace='app')),
    url(r'^minecraft/', include('mcoauth.mcaccounts.urls',
        namespace='minecraft')),
    url(r'^oauth2/', include('provider.oauth2.urls', namespace='oauth2')),
    url(r'^api/', include('mcoauth.api.urls', namespace='api')),
    url(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
