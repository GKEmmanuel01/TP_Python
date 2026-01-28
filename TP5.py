# TP 5 – Fichiers : lecture et écriture
# Sauvegarde et exploitation de données scolaires

# 1. Lecture des notes depuis le fichier
fichier_notes = open("notes.txt", "r")

notes = []
for ligne in fichier_notes:
    notes.append(float(ligne.strip()))

fichier_notes.close()

# 2. Calcul de la moyenne
somme = 0
for note in notes:
    somme += note

moyenne = somme / len(notes)

# 3. Écriture du résultat dans un fichier
fichier_resultat = open("resultat.txt", "w")
fichier_resultat.write("Moyenne de la classe : " + str(moyenne))
fichier_resultat.close()

print("Moyenne calculée et enregistrée dans resultat.txt")
