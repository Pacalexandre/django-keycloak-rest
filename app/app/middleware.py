from oic.oic import Client
from oic.utils.authn.client import CLIENT_AUTHN_METHOD
from oic import rndstr
from requests import session

class DjangoMiddlewareKeycloakOauth2:
    """Client oic authorization keycloak provider oauth2"""

    def __init__(self, get_response) -> None:
        issuer = "http://keycloak:8080/auth/realms/PALUNETWORK"
        client = Client()
        self.provider_info = client.provider_config(issuer)
        self.get_response = get_response
        self.session = {}
        self.session.update({"state": rndstr()})
        self.session.update({"nonce": rndstr()})


    def __call__(self,request):


        print('before response')
        authorization = request.headers
        print(authorization)
        print(self.provider_info)

        args = {
            "client_id": client.client_id,
            "response_type": "code",
            "scope": ["openid"],
            "nonce": self.session["nonce"],
            "redirect_uri": None,
            "state": self.session["state"]
        }

        auth_req = client.construct_AuthorizationRequest(request_args=args)
        login_url = auth_req.request(client.authorization_endpoint)

        return Redirect(login_url)

        response = self.get_response(request)

        print('after response')

        return response
    