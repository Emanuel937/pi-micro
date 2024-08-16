# Utiliser une image de base Python officielle
FROM python:latest

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier requirements.txt dans le conteneur
COPY requirements.txt .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Installer les dépendances nécessaires pour Selenium
RUN apt-get update && \
    apt-get install -y wget && \
    wget -q https://github.com/mozilla/geckodriver/releases/latest/download/geckodriver-v0.33.0-linux64.tar.gz && \
    tar -xzf geckodriver-v0.33.0-linux64.tar.gz && \
    mv geckodriver /usr/local/bin/ && \
    rm geckodriver-v0.33.0-linux64.tar.gz && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copier le reste du code source dans le conteneur
COPY . .

# Définir la commande par défaut à exécuter quand le conteneur démarre
CMD ["python", "app.py"]
