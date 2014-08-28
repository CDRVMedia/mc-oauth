from django.contrib.sites.models import RequestSite
from django.contrib.sites.models import Site

from registration import signals
from registration.backends.default.views import RegistrationView
from registration.models import RegistrationProfile

from .forms import RegistrationFormUniqueEmail


class RegistrationView(RegistrationView):
    """ Since we don't use usernames (only email addresses), we had
        to inherit this view to remove the username dependency.
    """
    form_class = RegistrationFormUniqueEmail
