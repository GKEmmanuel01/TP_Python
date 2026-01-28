# TP 3 – Listes, tuples et dictionnaires
# Gestion simplifiée des résultats académiques

# 1. Liste d'étudiants (chaque étudiant est un dictionnaire)
etudiants = [
    {"nom": "Alice", "age": 20, "moyenne": 12},
    {"nom": "Bob", "age": 18, "moyenne": 9},
    {"nom": "Claire", "age": 22, "moyenne": 15},
    {"nom": "David", "age": 19, "moyenne": 8},
    {"nom": "Emma", "age": 21, "moyenne": 11}
]

# 2. Afficher les étudiants admis (moyenne >= 10)
print("Étudiants admis :")
for etudiant in etudiants:
    if etudiant["moyenne"] >= 10:
        print(etudiant["nom"], "-", etudiant["moyenne"])

# 3. Calcul de la moyenne générale de la classe
somme = 0
for etudiant in etudiants:
    somme += etudiant["moyenne"]

moyenne_generale = somme / len(etudiants)
print("Moyenne générale de la classe :", moyenne_generale)
