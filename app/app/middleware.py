"Middleware Autenticated"

class DjangoMiddlewareKeycloakException(Exception):
    pass
    # message = {'content':'Request Bearer Token Authorization not in present'}


class DjangoMiddlewareKeycloakOauth2:
    """Client oic authorization keycloak provider oauth2"""

    def __init__(self, get_response) -> None:
        self.get_response = get_response
        self.session = {}

    def __call__(self,request):

        header = request.headers
        authorization = header.get('Authorization')
        if authorization is None:
            raise DjangoMiddlewareKeycloakException
        if 'Bearer' in authorization:
            token = authorization.split(' ')[1]

        print(token)

        response = self.get_response(request)

        print('after response')

        return response
    