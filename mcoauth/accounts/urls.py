from django.conf.urls import patterns, include, url

from .views import RegistrationView

urlpatterns = patterns(
    '',
    url(r'^register/$', RegistrationView.as_view(),
        name='registration_register'),
    url(r'^', include('registration.backends.default.urls')),
)
