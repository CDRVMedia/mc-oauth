from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from mcoauth.views import HomeView

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^oauth2/', include('provider.oauth2.urls', namespace='oauth2')),
)
