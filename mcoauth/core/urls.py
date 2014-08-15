from django.conf.urls import patterns, include, url

from .views import Home, Dashboard

urlpatterns = patterns(
    '',
    url(r'^$', Home.as_view(), name='home'),
    url(r'^dashboard/$', Dashboard.as_view(), name='dashboard'),
)
