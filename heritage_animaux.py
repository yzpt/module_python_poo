# Héritage et Polymorphisme en Python avec des animaux

# ┌──────────────────────┬────────────────────────────────────────────────────────┐
# │        Notion        │                       Explication                      │
# ├──────────────────────┼────────────────────────────────────────────────────────┤
# │ Classe parente       │ Classe de base dont les attributs et méthodes          │
# │                      │ peuvent être hérités par d'autres classes              │
# ├──────────────────────┼────────────────────────────────────────────────────────┤
# │ Classe enfant        │ Classe qui hérite des éléments (attributs/méthodes)    │
# │                      │ de la classe parente                                   │
# ├──────────────────────┼────────────────────────────────────────────────────────┤
# │ Héritage             │ `class Enfant(Parent)`                                 │
# │                      │ Permet à une classe d’hériter d’une autre              │
# ├──────────────────────┼────────────────────────────────────────────────────────┤
# │ Polymorphisme        │ Capacité pour différentes classes de redéfinir         │
# │                      │ une même méthode de façon adaptée à leur contexte      │
# └──────────────────────┴────────────────────────────────────────────────────────┘


# Classe parente : Animal
class Animal:
    def __init__(self, nom: str, age: int):
        self.nom = nom
        self.age = age

    def faire_du_bruit(self):
        print(f"{self.nom} fait un bruit.")

    def se_deplacer(self):
        print(f"{self.nom} se déplace.")

# Classe enfant : Chien
class Chien(Animal):
    def __init__(self, nom, age, race):
        super().__init__(nom, age)
        self.race = race

    # Polymorphisme : redéfinition spécifique du bruit
    def faire_du_bruit(self):
        print(f"{self.nom} aboie ! Woof woof !")

    def aboyer(self):
        print(f"{self.nom} aboie fort.")

# Classe enfant : Chat
class Chat(Animal):
    def __init__(self, nom, age, couleur):
        super().__init__(nom, age)
        self.couleur = couleur

    # Polymorphisme : redéfinition spécifique du bruit
    def faire_du_bruit(self):
        print(f"{self.nom} miaule ! Meow meow !")

    def ronronner(self):
        print(f"{self.nom} ronronne paisiblement.")

# Classe enfant : Oiseau
class Oiseau(Animal):
    def __init__(self, nom, age, espèce):
        super().__init__(nom, age)
        self.espèce = espèce

    # Polymorphisme : redéfinition spécifique du bruit
    def faire_du_bruit(self):
        print(f"{self.nom} chante ! Tweet tweet !")

    def voler(self):
        print(f"{self.nom} vole dans le ciel.")

# Utilisation des classes
animaux = [
    Chien("Rex", 5, "Labrador"),
    Chat("Mimi", 3, "Gris"),
    Oiseau("Tweety", 1, "Canari")
]

# Polymorphisme en action : même méthode appelée, comportement différent selon l'animal
for animal in animaux:
    animal.faire_du_bruit()  # Appelle la version spécifique à l'animal (Chien, Chat, Oiseau)
    animal.se_deplacer()     # Appelle la méthode de la classe parente

# Chaque animal peut aussi faire des actions spécifiques
animaux[0].aboyer()  # Appel spécifique à Chien
animaux[1].ronronner()  # Appel spécifique à Chat
animaux[2].voler()  # Appel spécifique à Oiseau
