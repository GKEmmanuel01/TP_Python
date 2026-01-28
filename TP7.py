# TP 7 – Programmation Orientée Objet (POO)
# Modélisation d’un système de gestion des étudiants

class Etudiant:
    # 1. Constructeur
    def __init__(self, nom, matricule, notes):
        self.nom = nom
        self.matricule = matricule
        self.notes = notes

    # 2. Méthode pour calculer la moyenne
    def calculer_moyenne(self):
        somme = 0
        for note in self.notes:
            somme += note
        return somme / len(self.notes)

    # 3. Méthode pour afficher les informations
    def afficher_infos(self):
        print("Nom :", self.nom)
        print("Matricule :", self.matricule)
        print("Notes :", self.notes)
        print("Moyenne :", self.calculer_moyenne())


# ----- Test du programme -----
etudiant1 = Etudiant("Alice", "ET001", [12, 14, 10])
etudiant2 = Etudiant("Bob", "ET002", [8, 9, 11])

etudiant1.afficher_infos()
print("------------------")
etudiant2.afficher_infos()
