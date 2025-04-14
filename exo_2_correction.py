## Exercice 2:

from datetime import datetime

class Personne:
    def __init__(self, nom, pays, date_naissance):
        self.nom = nom
        self.pays = pays
        self.date_naissance = datetime.strptime(date_naissance, "%Y-%m-%d")
        
    def afficher(self):
        print(f"Nom: {self.nom}, Pays: {self.pays}, Date de Naissance: {self.date_naissance.strftime('%Y-%m-%d')}")

    def age(self):
        today = datetime.today()
        age = today.year - self.date_naissance.year # (grossièrement)
        return age

# Création d'instances de la classe Personne:
personne1 = Personne("Alice", "France", "1990-05-15")
personne2 = Personne("Bob", "USA", "1985-10-20")

# Affichage des informations et de l'âge des personnes:
personne1.afficher()
print(f"Âge: {personne1.age()} ans")

