from flask import Flask, render_template, request
import requests
import random
import string

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


@app.route("/verify", methods=["GET", "POST"])
def verify_password_strength():
    if request.method == "POST":
        pass
    return render_template("verify.html")


def get_random_char():
    return random.choice(string.ascii_letters + string.digits + string.punctuation)


def get_random_number():
    return random.randint(0, 9)


def get_random_special_char():
    special_chars = string.punctuation
    return random.choice(special_chars)


def get_number_of_uppercase_letters(password):
    count = 0
    for char in password:
        if char.isupper():
            count += 1
    return count


def get_number_of_numbers(password):
    count = 0
    for char in password:
        if char.isdigit():
            count += 1
    return count


def get_number_of_special_chars(password):
    count = 0
    for char in password:
        if char in string.punctuation:
            count += 1
    return count


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
    app.run(debug=False)
