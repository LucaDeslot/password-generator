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


class TestPasswordImprovement(TestCase):
    def create_app(self):
        app.config["TESTING"] = True
        return app

    def test_improve_password_page(self):
        """Tests if the password generation page loads correctly."""
        response = self.client.get(url_for("improve_password"))
        self.assert200(response)
        self.assertTemplateUsed("improve.html")
        self.assertIn("Improve a Password", response.data.decode("utf-8"))

    def test_improve_password_functionality_valid(self):
        """Tests the password improvement functionality with a valid password."""
        # Test with a valid password
        valid_password = "StrongPassword123!"
        response = self.client.post(url_for("improve_password"), data={"password": valid_password})
        self.assert200(response)
        page_content = response.data.decode("utf-8")
        # Check if the text "Password improved:" is present in the page
        self.assertIn(
            "Password improved:",
            page_content,
            "Text 'Password improved:' not found in page content."
        )
        # Check if the improved password is displayed in the page
        self.assertIn(
            "<strong>",
            page_content,
            "Improved password not found in page content."
        )

    def test_improve_password_functionality_short(self):
        """Tests the password improvement functionality with a short password."""
        # Test with a short password
        short_password = "ShortPW"
        response = self.client.post(url_for("improve_password"), data={"password": short_password})
        self.assert200(response)
        page_content = response.data.decode("utf-8")
        # Check if the text "Password improved:" is present in the page
        self.assertIn(
            "Password improved:",
            page_content,
            "Text 'Password improved:' not found in page content."
        )
        # Check if the improved password is displayed in the page
        self.assertIn(
            "<strong>",
            page_content,
            "Improved password not found in page content."
        )
