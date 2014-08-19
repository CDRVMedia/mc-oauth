from django.utils.translation import ugettext as _
from provider.oauth2.forms import AuthorizationRequestForm


class AuthorizationRequestForm(AuthorizationRequestForm):
    def clean_redirect_uri(self):
        """
        Change original behavior to accept variable redirect_uri's
        """
        redirect_uri = self.cleaned_data.get('redirect_uri')

        if redirect_uri:
            if not redirect_uri.startswith(self.client.redirect_uri):
                raise OAuthValidationError({
                    'error': 'invalid_request',
                    'error_description': _("The requested redirect didn't "
                        "match the client settings.")})

        return redirect_uri
