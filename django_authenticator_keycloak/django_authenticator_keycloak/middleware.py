from .keycloak import KeycloakAuthorization


class AuthenticationMiddleware:
    
    def __init__(self, get_response) -> None:
        self.instance = KeycloakAuthorization().connect()

    def __call__(self, request):

        header = request.headers
        authorization = header.get('Authorization')
        if authorization is None:
            return
        if 'Bearer' in authorization:
            token = authorization.split(' ')[1]

        decoded = decode(token, options={"verify_signature": False})

        print(decoded)

        response = self.get_response(request)

        print('after response')

        return response