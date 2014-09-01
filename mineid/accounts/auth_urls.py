from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url

from django.contrib.auth import views as auth_views

from .forms import AuthenticationForm


urlpatterns = patterns(
    '',
   url(r'^login/$',
       auth_views.login,
       {'template_name': 'registration/login.html',
        'authentication_form': AuthenticationForm},
       name='login'),
   url(r'^logout/$',
       auth_views.logout,
       {'template_name': 'registration/logout.html'},
       name='logout'),
   url(r'^password/change/$',
       auth_views.password_change,
       name='password_change'),
   url(r'^password/change/done/$',
       auth_views.password_change_done,
       name='password_change_done'),
   url(r'^password/reset/$',
       auth_views.password_reset,
       name='password_reset'),
   url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
       auth_views.password_reset_confirm,
       name='password_reset_confirm'),
   url(r'^password/reset/complete/$',
       auth_views.password_reset_complete,
       name='password_reset_complete'),
   url(r'^password/reset/done/$',
       auth_views.password_reset_done,
       name='password_reset_done'),
)
