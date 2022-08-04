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
        "realm": "SSO-APP",
        "public_key": "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAgvnA4FsyN9Vhfa0BD5lVw7p7hAif7QP5YBCzCz1Bwnu+ZM4LsRn5I9zUU00VS8LOwBpqmXsLrw+ZzuzcmjLvxQSwPpgnzm+3s0ppHHyEOJuCjVoez5k84IDN5e7jA7wiPtESEgxWOo5SQHmgrR+zmew9rXY4SMBPP61lEHfH/iJV7T/+4GnLuw8SxSV//5dV6uT+ZmCHAj9yAf0LnF15WifBunxSUbh3rjDMNT+yZD/vQHURF6wLacI7GzXYy+FVpTnHr592KIUpNvdfZJFQPIr7WQSARAf6Y0wZdeUgG4c0S+wUlGFV6qS1XnluvNnDtXLl6pOurQ8i979VcKpGtQIDAQAB",
        "token-service": "http://localhost:8080/auth/realms/SSO-APP/protocol/openid-connect",
        "account-service": "http://localhost:8080/auth/realms/SSO-APP/account",
        "tokens-not-before": 0
        }
    provider = client.provider_config(issuer)
    valor = True
    return valor
