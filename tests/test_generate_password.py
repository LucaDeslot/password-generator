from flask_testing import TestCase
from flask import url_for
from app import (
    app,
)


class TestPasswordGeneration(TestCase):
    def create_app(self):
        app.config["TESTING"] = True
        return app

    def test_generate_password_page(self):
        """Tests if the password generation page loads correctly."""
        response = self.client.get(url_for("generate_password"))
        self.assert200(response)
        self.assertTemplateUsed("generate.html")
        self.assertIn("Generate a Password", response.data.decode("utf-8"))

    def test_generate_password_functionality(self):
        """Tests the password generation functionality via a POST request."""
        test_length = 12
        response = self.client.post(
            url_for("generate_password"), data={"length": str(test_length)}
        )
        self.assert200(response)
        page_content = response.data.decode("utf-8")
        self.assertIn(
            "Password generated:",
            page_content or "Error generating password.",
            page_content,
        )
