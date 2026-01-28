# TP 4 – Manipulation de chaînes de caractères
# Analyse de commentaires saisis par des utilisateurs

# 1. Demander une phrase à l'utilisateur
phrase = input("Entrez une phrase : ")

# 2. Compter le nombre de mots
mots = phrase.split()
nb_mots = len(mots)
print("Nombre de mots :", nb_mots)

# 3. Trouver le mot le plus long
mot_plus_long = ""
for mot in mots:
    if len(mot) > len(mot_plus_long):
        mot_plus_long = mot

print("Mot le plus long :", mot_plus_long)

# 4. Vérifier si la phrase est un palindrome
phrase_nettoyee = phrase.replace(" ", "").lower()

if phrase_nettoyee == phrase_nettoyee[::-1]:
    print("La phrase est un palindrome.")
else:
    print("La phrase n'est pas un palindrome.")
