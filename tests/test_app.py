import pytest
from flask_testing import TestCase

from app import app  # Assurez-vous que cela correspond au chemin d'importation de votre application Flask


class MyTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_root_route(self):
        response = self.client.get('/')
        self.assert200(response)  # Vérifie que la réponse a un statut 200 OK
        self.assertEqual(response.data.decode('utf-8'), 'Hello World!')  # Vérifie le contenu de la réponse


if __name__ == '__main__':
    pytest.main()
