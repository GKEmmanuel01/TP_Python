

import time


def tri_bulles(liste):
    n = len(liste)
    for i in range(n):
        for j in range(0, n - i - 1):
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
    return liste



def recherche_lineaire(liste, valeur):
    for i in range(len(liste)):
        if liste[i] == valeur:
            return i
    return -1


liste = [12, 5, 8, 3, 15, 7, 10, 1, 9]
valeur_recherchee = 15


liste1 = liste.copy()
debut = time.time()
tri_bulles(liste1)
fin = time.time()
print("Tri à bulles :", liste1)
print("Temps tri à bulles :", fin - debut)


liste2 = liste.copy()
debut = time.time()
liste2.sort()
fin = time.time()
print("Tri Python :", liste2)
print("Temps tri Python :", fin - debut)


debut = time.time()
position = recherche_lineaire(liste, valeur_recherchee)
fin = time.time()
print("Recherche linéaire : position =", position)
print("Temps recherche linéaire :", fin - debut)


debut = time.time()
position_python = liste.index(valeur_recherchee)
fin = time.time()
print("Recherche Python : position =", position_python)
print("Temps recherche Python :", fin - debut)
