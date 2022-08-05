from keycloak import KeycloakAuthorization
from django.test import TestCase


class KeycloakTest(TestCase):
    def setUp(self):
        pass

    def test_animals_can_speak(self):
        instance = KeycloakAuthorization()
        self.assertIsInstance(instance, KeycloakAuthorization)