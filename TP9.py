# TP 9 – Manipulation de données CSV

import csv


salaires_par_departement = {}
effectifs = {}

with open("employes.csv", "r", newline="", encoding="utf-8") as fichier:
    lecteur = csv.DictReader(fichier)
    for ligne in lecteur:
        departement = ligne["departement"]
        salaire = float(ligne["salaire"])

        if departement not in salaires_par_departement:
            salaires_par_departement[departement] = 0
            effectifs[departement] = 0

        salaires_par_departement[departement] += salaire
        effectifs[departement] += 1


moyennes = {}
for departement in salaires_par_departement:
    moyennes[departement] = (
        salaires_par_departement[departement] / effectifs[departement]
    )


with open("rapport.txt", "w", encoding="utf-8") as rapport:
    rapport.write("Rapport des salaires moyens par département\n")
    rapport.write("------------------------------------------\n")
    for departement, moyenne in moyennes.items():
        rapport.write(f"{departement} : {moyenne} FCFA\n")

print("Rapport généré avec succès dans rapport.txt")
