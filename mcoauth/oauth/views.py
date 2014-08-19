from provider.oauth2.views import Authorize
from .forms import AuthorizationRequestForm


class Authorize(Authorize):
    def get_request_form(self, client, data):
        return AuthorizationRequestForm(data, client=client)
