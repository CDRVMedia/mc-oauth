from django.conf.urls import patterns, include, url

from .views import RegistrationView, RegistrationComplete, SetEmailAddress

urlpatterns = patterns(
    '',
    url(r'^register/$', RegistrationView.as_view(),
        name='registration_register'),
    url(r'^register/complete/$',
        RegistrationComplete.as_view(),
        name='registration_complete'),
    url(r'^', include('mcoauth.accounts.auth_urls')),
    url(r'^', include('registration.backends.default.urls')),
    url(r'^set_email_address/$', SetEmailAddress.as_view(),
        name='set_email_address'),
)
