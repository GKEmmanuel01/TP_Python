# TP 2 – Fonctions et modularité
# Automatisation du calcul des moyennes d’une classe

# 1. Fonction pour calculer la moyenne
def calcul_moyenne(liste_notes):
    somme = 0
    for note in liste_notes:
        somme += note
    moyenne = somme / len(liste_notes)
    return moyenne


# 2. Fonction pour déterminer la mention
def mention(moyenne):
    if moyenne < 10:
        return "Ajourné"
    elif moyenne < 12:
        return "Passable"
    elif moyenne < 16:
        return "Bien"
    else:
        return "Très bien"


# 3. Tests avec plusieurs listes de notes
notes1 = [10, 12, 14]
notes2 = [8, 9, 7]
notes3 = [15, 16, 18]

moy1 = calcul_moyenne(notes1)
moy2 = calcul_moyenne(notes2)
moy3 = calcul_moyenne(notes3)

print("Notes :", notes1, "→ Moyenne :", moy1, "→ Mention :", mention(moy1))
print("Notes :", notes2, "→ Moyenne :", moy2, "→ Mention :", mention(moy2))
print("Notes :", notes3, "→ Moyenne :", moy3, "→ Mention :", mention(moy3))
