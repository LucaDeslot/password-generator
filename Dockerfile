FROM python:3.12-slim

WORKDIR /app

# Copiez les fichiers de dépendances
COPY requirements.txt .

# Installez les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copiez le reste de votre code d'application
COPY . .

EXPOSE 5000

# Commande pour exécuter l'application
CMD ["flask", "run", "--host=0.0.0.0"]
