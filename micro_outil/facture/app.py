from flask import Flask, render_template, jsonify
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello_world():
    # Configurer les options de Firefox pour le mode sans tête
    firefox_options = Options()
    firefox_options.add_argument("--headless")

    # Initialiser le driver Firefox avec les options configurées
    driver = webdriver.Firefox()
    driver.get("https://www.google.com/")
    
    # Attendre que la page se charge et accepter les cookies
    time.sleep(1)
    
    # Vérifier si le bouton d'acceptation des cookies est présent avant de cliquer
    try:
        accept_condition = driver.find_element(By.CSS_SELECTOR, "button#L2AGLb")
        accept_condition.click()
    except Exception as e:
        print(f"Error: {e}")
    
    title = driver.title
    driver.quit()
    
    # Retourner le titre de la page en JSON
    return jsonify({"title": title})

@app.route("/login", methods=['GET'])
def login():
    return render_template("login.html")

if __name__ == '__main__':
    app.run(debug=True)
