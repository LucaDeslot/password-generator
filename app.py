import re

from flask import Flask, render_template, request, jsonify
import requests
import random

from utils import get_random_char, get_random_number, get_random_special_char, get_number_of_uppercase_letters, \
    get_number_of_numbers, get_number_of_special_chars

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["GET", "POST"])
def generate_password():
    if request.method == "POST":
        length = request.form.get("length", "20")

        api_url = f"https://password.ninja/api/password?minPassLength={length}"

        response = requests.get(api_url)
        if response.status_code == 200:
            password = response.text
        else:
            password = "Erreur lors de la génération du mot de passe."

        return render_template("generate.html", password=password)

    return render_template("generate.html", password=None)

@app.route("/verify", methods=["GET"])
def verify():
    return render_template("verify.html")

def check_password_strength(password):
    # Critères de solidité
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"\W", password) is None

    # Évaluation de la solidité
    strength = 'Strong'
    criteria = {
        "length": "au moins 8 caractères",
        "digit": "contenir un chiffre",
        "uppercase": "contenir une majuscule",
        "lowercase": "contenir une minuscule",
        "symbol": "contenir un caractère spécial"
    }
    missing_criteria = []

    if length_error or digit_error or uppercase_error or lowercase_error or symbol_error:
        strength = 'Weak'
        if length_error:
            missing_criteria.append(criteria["length"])
        if digit_error:
            missing_criteria.append(criteria["digit"])
        if uppercase_error:
            missing_criteria.append(criteria["uppercase"])
        if lowercase_error:
            missing_criteria.append(criteria["lowercase"])
        if symbol_error:
            missing_criteria.append(criteria["symbol"])

    # Améliorer la classification si nécessaire
    if len(missing_criteria) <= 2 and not length_error:
        strength = 'Medium' if strength == 'Weak' else strength

    return {"result": strength, "missing": missing_criteria}

@app.route("/verify_password_strength", methods=["POST"])
def verify_password_strength():
    data = request.get_json()
    password = data.get("password", "")
    strength_evaluation = check_password_strength(password)
    return jsonify(strength_evaluation)

@app.route("/improve", methods=["GET", "POST"])
def improve_password():
    if request.method == "POST":
        password = request.form.get("password", "")

        while len(password) < 12:
            password += str(get_random_number())
            password += get_random_char()
            password += get_random_special_char()

        while get_number_of_uppercase_letters(password) < 3:
            random_number = random.randint(0, len(password) - 1)
            password = password[:random_number] + password[random_number].upper() + password[random_number + 1:]

        while get_number_of_numbers(password) < 3:
            password += str(get_random_number())

        while get_number_of_special_chars(password) < 3:
            password += get_random_special_char()

        return render_template("improve.html", password=password)

    return render_template("improve.html", password=None)


if __name__ == "__main__":
    app.run(debug=True)
