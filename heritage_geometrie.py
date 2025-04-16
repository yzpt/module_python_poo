# 🧠 POO : Classe, Héritage, Polymorphisme

# ┌──────────────────────┬────────────────────────────────────────────────────────┐
# │       Notion         │                        Explication                     │
# ├──────────────────────┼────────────────────────────────────────────────────────┤
# │ Classe parente       │ Classe de base contenant des attributs/méthodes        │
# │                      │ génériques pour toutes les formes                      │
# ├──────────────────────┼────────────────────────────────────────────────────────┤
# │ Classe enfant        │ Hérite de la classe parente et peut redéfinir ou       │
# │                      │ étendre ses fonctionnalités                            │
# ├──────────────────────┼────────────────────────────────────────────────────────┤
# │ Polymorphisme        │ Une même méthode (ex: surface) se comporte             │
# │                      │ différemment selon la classe de l’objet                │
# └──────────────────────┴────────────────────────────────────────────────────────┘


# ✨ Classe de base : Forme
class Forme:
    def afficher(self):
        print("🔺 Ceci est une forme géométrique.")
    
    def surface(self):
        print("Méthode à implémenter dans les sous-classes.")
        pass

    def perimetre(self):
        print('Méthode à implémenter dans les sous-classes.')
        pass


# 🟦 Rectangle hérite de Forme
class Rectangle(Forme):
    def __init__(self, largeur, longueur):
        self.largeur = largeur
        self.longueur = longueur

    def afficher(self):
        print(f"🟦 Rectangle - Largeur: {self.largeur}, Longueur: {self.longueur}")

    def surface(self):
        return self.largeur * self.longueur

    def perimetre(self):
        return 2 * (self.largeur + self.longueur)


# ⚪ Cercle hérite de Forme
import math

class Cercle(Forme):
    def __init__(self, rayon):
        self.rayon = rayon

    def afficher(self):
        print(f"⚪ Cercle - Rayon: {self.rayon}")

    def surface(self):
        return math.pi * self.rayon ** 2

    def perimetre(self):
        return 2 * math.pi * self.rayon


# 🔺 Triangle hérite de Forme
class Triangle(Forme):
    def __init__(self, base, hauteur, cote1, cote2):
        self.base = base
        self.hauteur = hauteur
        self.cote1 = cote1
        self.cote2 = cote2

    def afficher(self):
        print(f"🔺 Triangle - Base: {self.base}, Hauteur: {self.hauteur}")

    def surface(self):
        return 0.5 * self.base * self.hauteur

    def perimetre(self):
        return self.base + self.cote1 + self.cote2


# 🔁 Utilisation polymorphe : une liste de formes
formes = [
    Rectangle(5, 10),
    Cercle(7),
    Triangle(6, 4, 5, 5)
]

# 🧪 Affichage polymorphe : on appelle les mêmes méthodes sur chaque objet
for forme in formes:
    forme.afficher()                                 # Méthode spécifique à chaque forme
    print(f"📐 Surface : {forme.surface():.2f}")
    print(f"📏 Périmètre : {forme.perimetre():.2f}\n")
