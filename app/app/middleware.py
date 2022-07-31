class DjangoMiddlewareKeycloakOauth2:
    def __init__(self, get_response) -> None:
        self.get_response = get_response


    def __call__(self,request):

        print('before response')
        authorization = request.headers
        print(authorization)

        response = self.get_response(request)

        print('after response')

        return response
    