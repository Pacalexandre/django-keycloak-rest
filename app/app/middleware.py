"Middleware Autenticated"
from jwt import decode


class DjangoMiddlewareKeycloakException(Exception):
    pass
    # message = {'content':'Request Bearer Token Authorization not in present'}


class DjangoMiddlewareKeycloakOauth2:
    """Client oic authorization keycloak provider oauth2"""

    def __init__(self, get_response) -> None:
        self.get_response = get_response
        self.session = {}

    def __call__(self, request):

        header = request.headers
        authorization = header.get('Authorization')
        if authorization is None:
            raise DjangoMiddlewareKeycloakException
        if 'Bearer' in authorization:
            token = authorization.split(' ')[1]

        decoded = decode(token, options={"verify_signature": False})

        print(decoded)

        response = self.get_response(request)

        print('after response')

        return response

        # encoded = jwt.encode({"some": "payload"}, "secret", algorithm="HS256")
        # print(encoded)
        # eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzb21lIjoicGF5bG9hZCJ9.Joh1R2dYzkRvDkqv3sygm5YyK8Gi4ShZqbhK2gxcs2U

        #decode(self.bearer_token, options={"verify_signature": False})
