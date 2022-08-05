import logging, requests
from django.conf import settings

LOGGER = logging.getLogger(__name__)


class KeycloakAuthorization:
    # instance
    def __init__(self):
        # Set configurations from the settings file
        self.config = settings.KEYCLOAK_CONFIG

        # Read keycloak configurations and set each attribute
        try:
            self.server_url = self.config['KEYCLOAK_SERVER_URL']
            self.realm = self.config['KEYCLOAK_REALM']
            self.client_id = self.config['KEYCLOAK_CLIENT_ID']
            self.client_secret_key = self.config['KEYCLOAK_CLIENT_SECRET_KEY']
        except KeyError:
            raise Exception("The mandatory KEYCLOAK configuration variables has not defined.")

        if self.config['KEYCLOAK_SERVER_URL'] is None:
            raise Exception("The mandatory KEYCLOAK_SERVER_URL configuration variables has not defined.")

        if self.config['KEYCLOAK_REALM'] is None:
            raise Exception("The mandatory KEYCLOAK_REALM configuration variables has not defined.")

        if self.config['KEYCLOAK_CLIENT_ID'] is None:
            raise Exception("The mandatory KEYCLOAK_CLIENT_ID configuration variables has not defined.")

        if self.config['KEYCLOAK_CLIENT_SECRET_KEY'] is None:
            raise Exception("The mandatory KEYCLOAK_CLIENT_SECRET_KEY configuration variables has not defined.")

        # url base connection keycloak
        self.kc_url_realms =f'{self.server_url}/realms/{self.realm}'


    # Keycloak useful Urls
    def get_well_known(self):
        """Lists endpoints and other configuration options
         relevant to the OpenID Connect implementation in Keycloak.
        Returns:
            [type]: [list of keycloak endpoints]
        """
        url = f'{self.kc_url_realms}/.well-known/openid-configuration'
        response = requests.request("GET", url)
        error = response.raise_for_status()
        if error:
            LOGGER.error("Error obtaining list of endpoints from endpoint: %s - %s",
                url, error, exc_info=1)
            return {}
        return response.json()


    def get_introspect(self):
        return f'{self.kc_url_realms}/protocol/openid-connect/token/introspect'

    def get_userinfo(self):
        return f'{self.kc_url_realms}/protocol/openid-connect/userinfo'
