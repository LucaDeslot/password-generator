from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/generate', methods=['GET', 'POST'])
def generate_password():
    if request.method == 'POST':
        # Récupère la longueur du mot de passe depuis le formulaire
        length = request.form.get('length', '20')

        # Construit l'URL avec le paramètre de longueur
        api_url = f'https://password.ninja/api/password?minPassLength={length}'

        # Appel à l'API pour obtenir un mot de passe
        response = requests.get(api_url)
        if response.status_code == 200:
            password = response.text
        else:
            password = "Erreur lors de la génération du mot de passe."

        # Renvoie la même page avec le mot de passe généré affiché
        return render_template('generate.html', password=password)

    # Pour une requête GET, affiche simplement le formulaire sans mot de passe
    return render_template('generate.html', password=None)

@app.route('/verify', methods=['GET', 'POST'])
def verify_password_strength():
    if request.method == 'POST':
        # Ici, intégrez la logique pour vérifier la force du mot de passe soumis par l'utilisateur
        pass  # Remplacez cette ligne par votre code
    # Affiche le formulaire pour vérifier la force d'un mot de passe
    return render_template('verify.html')

@app.route('/strengthen', methods=['GET', 'POST'])
def strengthen_password():
    if request.method == 'POST':
        # Ici, intégrez la logique pour renforcer un mot de passe soumis par l'utilisateur
        pass  # Remplacez cette ligne par votre code
    # Affiche le formulaire pour renforcer un mot de passe
    return render_template('strengthen.html')

if __name__ == '__main__':
    app.run(debug=True)

#
# @app.route('/', methods=['GET'])
# def generate_password():
#     # Lit la longueur du mot de passe depuis la requête, avec une valeur par défaut de 20
#     length = request.args.get('length', '20')
#
#     # Construit l'URL avec le paramètre de longueur
#     api_url = f'https://password.ninja/api/password?minPassLength={length}'
#
#     # Appel à l'API pour obtenir un mot de passe
#     response = requests.get(api_url)
#     if response.status_code == 200:
#         password = response.text
#     else:
#         password = "Erreur lors de la génération du mot de passe."
#
#     # Renvoie une page HTML avec le mot de passe généré
#     return render_template('index.html', password=password)


if __name__ == '__main__':
    app.run(debug=True)
