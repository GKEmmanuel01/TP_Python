# TP 6 – Gestion des exceptions
# Sécurisation d'une application pour non-informaticiens

try:
    # 1. Saisie des valeurs
    a = float(input("Entrez le numérateur : "))
    b = float(input("Entrez le dénominateur : "))

    # 2. Division
    resultat = a / b
    print("Résultat de la division :", resultat)

except ZeroDivisionError:
    print("Erreur : division par zéro interdite.")

except ValueError:
    print("Erreur : veuillez entrer des nombres valides.")

finally:
    print("Fin du programme.")
