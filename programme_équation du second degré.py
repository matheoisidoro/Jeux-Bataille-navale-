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