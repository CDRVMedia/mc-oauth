from django.core import signing
from django.utils.translation import ugettext as _

from provider.oauth2.views import Authorize, AccessTokenView

from .forms import AuthorizationRequestForm


class Authorize(Authorize):
    def get_request_form(self, client, data):
        return AuthorizationRequestForm(data, client=client)

    def get_data(self, request, key='params'):
        switch_account = request.COOKIES.get('switch_account')

        if switch_account:
            try:
                data = signing.loads(switch_account)
                self.cache_data(request, data)
                return data
            except signing.BadSignature:
                pass

        return super(Authorize, self).get_data(request, key=key)

    def get(self, request, *args, **kwargs):
        response = super(Authorize, self).get(request, *args, **kwargs)

        if 'switch_account' in request.COOKIES:
            response.delete_cookie('switch_account')

        return response


from provider.views import constants
from logging import getLogger

logger = getLogger(__name__)

class AccessTokenView(AccessTokenView):
    def post(self, request):
        """
        As per :rfc:`3.2` the token endpoint *only* supports POST requests.
        """
        logger.debug('Received Access Token request: %s' % (
            request.POST.get('grant_type', '<>')))

        if constants.ENFORCE_SECURE and not request.is_secure():
            return self.error_response({
                'error': 'invalid_request',
                'error_description': _("A secure connection is required.")})

        if not 'grant_type' in request.POST:
            return self.error_response({
                'error': 'invalid_request',
                'error_description': _("No 'grant_type' included in the "
                    "request.")})

        grant_type = request.POST['grant_type']

        if grant_type not in self.grant_types:
            return self.error_response({'error': 'unsupported_grant_type'})

        client = self.authenticate(request)

        if client is None:
            logger.debug('Client not authenticated')
            return self.error_response({'error': 'invalid_client'})

        logger.debug('Client identified: %s' % client.client_id)

        handler = self.get_handler(grant_type)

        logger.debug('Processing handler: %s' % handler)

        try:
            return handler(request, request.POST, client)
        except OAuthError, e:
            logger.debug('handler error: ' % e.args[0], exc_info=True)
            return self.error_response(e.args[0])
