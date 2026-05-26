# On part d'une image Python légère
FROM python:3.11-slim

# On définit le dossier de travail dans le conteneur
WORKDIR /app

# On copie le fichier de dépendances en premier (optimisation du cache Docker)
COPY requirements.txt .

# On installe les bibliothèques requises
RUN pip install --no-cache-dir -r requirements.txt

# On copie le reste des fichiers du projet (ici, app.py)
COPY . .

# La commande exécutée par défaut au lancement du conteneur
CMD ["python", "app.py"]
