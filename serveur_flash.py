from flask import Flask, send_file
import os

app = Flask(__name__)

@app.route('/telecharger_jeu', methods=['GET'])
def telecharger_jeu():
    chemin_fichier = "C:/Users/mathe/OneDrive/Bureau/Projet Btaille naval/programme_équation du second degré.py"
    return send_file(chemin_fichier, as_attachment=True)

if __name__ == '__main__':
    app.run(port=8080)