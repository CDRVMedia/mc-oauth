import logging


logger = logging.getLogger(__name__)


class MinecraftBackend(object):
    def authenticate(username, password):
        url = 'https://authserver.mojang.com/authenticate'

        payload = {
            'agent': {
                'name': 'Minecraft',
                'version': 1,
            },
            'username': username,
            'password': password,
        }

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }
        import pdb; pdb.set_trace()

        try:
            request = urllib2.Request(url, json.dumps(payload), headers)
            response = urlopen(request)

            try:
                response_payload = json.loads(response.read())

            finally:
                response.close()  # always close socket

            return response_payload

        except urllib2.HTTPError as e:
            minecraftException = MinecraftAuthenticationException(e)

            if 'test' not in sys.argv:
                _msg = 'Mojang authentication failed for %s: "%s"'
                logger.debug(_msg % (username, minecraftException.message))

            raise minecraftException
