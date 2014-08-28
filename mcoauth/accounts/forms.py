from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model

from registration.forms import RegistrationForm

User = get_user_model()


class RegistrationForm(RegistrationForm):
    """ Note: These forms were inherited only to remove
        the username dependency
    """
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        del self.fields['username']


class RegistrationFormUniqueEmail(RegistrationForm):
    def clean_email(self):
        if User.objects.filter(email__iexact=self.cleaned_data['email']):
            raise forms.ValidationError(
                _(
                    "This email address is already in use. "
                    "Please supply a different email address."
                ))
        return self.cleaned_data['email']

    def clean(self):
        cleaned_data = super(RegistrationFormUniqueEmail, self).clean()
        cleaned_data['username'] = cleaned_data.get('email')
        return cleaned_data
