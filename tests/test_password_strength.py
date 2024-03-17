import pytest
from flask_testing import TestCase
from app import (
    app,
)
class TestPasswordStrength(TestCase):

    def create_app(self):
        # Configurez votre application Flask pour les tests
        app.config['TESTING'] = True
        return app

    def test_password_strength_weak(self):
        response = self.client.post('/verify_password_strength', json={'password': '123'})
        self.assert200(response)
        data = response.json
        assert data['result'] == 'Weak'

    def test_password_strength_strong(self):
        response = self.client.post('/verify_password_strength', json={'password': 'StrongPass1!'})
        self.assert200(response)
        data = response.json
        print(data)
        assert data['result'] == 'Strong'

    def test_password_missing_criteria(self):
        response = self.client.post('/verify_password_strength', json={'password': 'Strong1'})
        self.assert200(response)
        data = response.json
        assert 'missing' in data
        assert 'contenir un caractère spécial' in data['missing']

