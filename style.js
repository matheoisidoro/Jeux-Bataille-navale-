function downloadGame() {
    // Générez le contenu du fichier Python
    var pythonCode = `
from math import sqrt

def valeur ():
    a = float(input("Choisir la valeur a: "))
    b = float(input("Choisir la valeur b: "))
    c = float(input("Choisir la valeur c: "))

    return a, b, c

def delta(a, b, c):
    return b**2-(4*a*c)

def calcule (delta, a, b):
    if delta <0:
        print("Pas de solutions pour cette équation")

    elif delta == 0:
        x1 = -b/2*a
        print("Solution de x1 est", x1)

    else :
        x1 = (-b+sqrt(delta))/(2*a)
        x2 = (-b-sqrt(delta))/(2*a)
        print("Solution de x1 est",x1)
        print("Solution de x2 est",x2)

a, b, c = valeur()
d = delta(a, b, c)
calcule(d, a, b)

while True:
    if input("voulez vous continuer?")=="non":
        break

    a, b, c = valeur()
    d = delta(a, b, c)
    calcule(d, a, b)

`;

    // Créez un objet Blob avec le contenu du fichier Python
    var blob = new Blob([pythonCode], { type: 'text/python' });

    // Créez un objet URL pour le Blob
    var url = window.URL.createObjectURL(blob);

    // Créez un lien temporaire
    var link = document.createElement('a');
    link.href = url;

    // Spécifiez le nom du fichier lors du téléchargement
    link.download = 'jeux_de_la bataille_navale.py';

    // Ajoutez le lien à la page
    document.body.appendChild(link);

    // Simulez un clic sur le lien pour déclencher le téléchargement
    link.click();

    // Supprimez le lien de la page
    document.body.removeChild(link);

    // Révoquez l'URL pour libérer des ressources
    window.URL.revokeObjectURL(url);
}

