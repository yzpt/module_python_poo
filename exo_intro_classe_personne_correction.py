# Créer une classe Personne, qui comporte:
# - Les attributs :
#     - nom
#     - prénom
#     - date de naissance
#     - statut : (étudiant, personnel, formateur)
#     - 
# - Les méthodes :
#     - constructeur (__init__)
#     - méthode se_presenter() (par exemple : "Bonjour je m'appelle Manon, je travaille à l'école GEMA"; "Bonjour je m'appelle Edouard, j'étudie à l'école GEMA", "Bonjour je m'appelle Yohann et je donne des cours dans l'école GEMA, uniquement aux beaux-gosses", etc).
    
#     - Calculer l'âge actuel de la personne (voir fichier datetime_calculer_age.py), l'inclure dans la présentation.

from datetime import datetime

class Personne:
    def __init__(self, nom, prenom, date_naissance, statut):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.statut = statut
        
    def calculer_age(self):
        today = datetime.now()
        age = today.year - self.date_naissance.year - ((today.month, today.day) < (self.date_naissance.month, self.date_naissance.day))
        return age
    
    def se_presenter(self):
        if self.statut == "étudiant":
            return f"Bonjour, je m'appelle {self.prenom} {self.nom}, j'étudie à l'école GEMA et j'ai {self.calculer_age()} ans."
        elif self.statut == "personnel":
            return ...
        elif self.statut == "formateur":
            return ...
        
        
# Tester son code :
# Créer une instance de la classe Personne
p1 = Personne("Dupont", "Jean", datetime(2006, 5, 15), "étudiant")
p2 = Personne("Martin", "Sophie", datetime(1985, 3, 22), "personnel")
p3 = Personne("Durand", "Pierre", datetime(1980, 12, 1), "formateur")

# Afficher la présentation de chaque personne
print(p1.se_presenter())
print(p2.se_presenter())
print(p3.se_presenter())