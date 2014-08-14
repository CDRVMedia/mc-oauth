from django.contrib.sites.models import RequestSite
from django.contrib.sites.models import Site

from registration import signals
from registration.backends.default.views import RegistrationView
from registration.models import RegistrationProfile

from .forms import RegistrationFormUniqueEmail


class RegistrationView(RegistrationView):
    form_class = RegistrationFormUniqueEmail

    def register(self, request, **cleaned_data):
        email, password = cleaned_data['email'], cleaned_data['password1']
        if Site._meta.installed:
            site = Site.objects.get_current()
        else:
            site = RequestSite(request)
        new_user = RegistrationProfile.objects.create_inactive_user(
            None, email, password, site)
        signals.user_registered.send(sender=self.__class__, user=new_user,
                                     request=request)
        return new_user
