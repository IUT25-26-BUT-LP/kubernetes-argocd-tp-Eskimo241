from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Statut : Pipeline DevSecOps Opérationnel !</h1><p>Image vérifiée et déployée par ArgoCD.</p>"

if __name__ == "__main__":
    # On écoute sur le port 8080
    app.run(host='0.0.0.0', port=8080)