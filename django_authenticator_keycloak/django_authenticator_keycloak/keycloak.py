# import requests
# from django.conf import settings
from oic.oic import Client
from oic.utils.authn.client import CLIENT_AUTHN_METHOD


#class KeycloakAuthorization:
    # """ Keycloak Authorization - flow OpenID Connect """
    # def __init__(self) -> None:
    #     # Set configurations from the settings file
        # self.config = settings.KEYCLOAK_CONFIG
        # # set require configurations
        # self.server_url = self.config.get('KEYCLOAK_SERVER_URL', None)
        # self.realm_name = self.config.get('KEYCLOAK_REALM', None)
        # self.client_id = self.config.get('KEYCLOAK_CLIENT_ID', None)
        # self.client_secret_key = self.config.get('KEYCLOAK_CLIENT_SECRET_KEY', None)
        # Set
    
def connect():
    client = Client(client_authn_method=CLIENT_AUTHN_METHOD)
    issuer = {
        "realm": "",
        "public_key":"" ,
        "token-service": "",
        "account-service": "",
        "tokens-not-before": 0
        }
    provider = client.provider_config(issuer)
    valor = True
    return valor
