from flask import Flask, render_template, request
import requests
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


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
            password = "Error while generating password"

        return render_template("generate.html", password=password)

    return render_template("generate.html", password=None)


@app.route("/verify", methods=["GET", "POST"])
def verify_password_strength():
    if request.method == "POST":
        pass
    return render_template("verify.html")


@app.route("/strengthen", methods=["GET", "POST"])
def strengthen_password():
    if request.method == "POST":
        pass
    return render_template("strengthen.html")


if __name__ == "__main__":
    app.run(port=5000)
