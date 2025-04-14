## Exercice 2:
# Écrivez un programme Python pour créer une classe Personne. Incluez des attributs tels que le nom, le pays et la date de naissance. 
# Implémentez une méthode pour déterminer l’âge de la personne (utiliser la biblothèque datetime, chatgpt)

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
    
