from .keycloak import connect # KeycloakAuthorization


class Authentication:
    
    def __init__(self, get_response) -> None:
        self.get_response = get_response

    def __call__(self, request):
        header = request.headers
        authorization = header.get('Authorization')
        if authorization is None:
            return
        if 'Bearer' in authorization:
            token = authorization.split(' ')[1]
            self.instance = connect()

        # decoded = decode(token, options={"verify_signature": False})

        print(token)

        response = self.get_response(request)

        print('after response')

        return response