import requests
from django.conf import settings

class KeycloakAuthorization:
    """ Keycloak Authorization - flow OpenID Connect """
    def __init__(self) -> None:
        # Set configurations from the settings file
        self.config = settings.KEYCLOAK_CONFIG
        # set require configurations 
        self.server_url = self.config.get('KEYCLOAK_SERVER_URL', None)
        self.realm_name = self.config.get('KEYCLOAK_REALM', None)
        self.client_id = self.config.get('KEYCLOAK_CLIENT_ID', None)
        self.client_secret_key = self.config.get('KEYCLOAK_CLIENT_SECRET_KEY', None)
        
    def connect(self):

        return instance