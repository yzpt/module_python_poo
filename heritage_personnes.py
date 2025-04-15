# Héritage et Polymorphisme en Python

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


# Classe parente
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def se_presenter(self):
        print(f"👋 Bonjour, je m'appelle {self.nom} et j'ai {self.age} ans.")


# Classe enfant : Élève
class Eleve(Personne):
    def __init__(self, nom, age, niveau):
        super().__init__(nom, age)
        self.niveau = niveau

    # Polymorphisme : on redéfinit se_presenter de manière plus spécifique
    def se_presenter(self):
        print(f"🎒 Je suis l'élève {self.nom}, j'ai {self.age} ans, et je suis en {self.niveau}.")

    def etudier(self):
        print(f"📚 {self.nom} étudie au niveau {self.niveau}.")


# Classe enfant : Personnel
class Personnel(Personne):
    def __init__(self, nom, age, poste):
        super().__init__(nom, age)
        self.poste = poste

    # Polymorphisme : redéfinition personnalisée
    def se_presenter(self):
        print(f"🏫 Je suis {self.nom}, j'ai {self.age} ans, et je suis {self.poste}.")

    def travailler(self):
        print(f"🛠️ {self.nom} travaille comme {self.poste}.")


# Utilisation des classes
personnes = [
    Eleve("Pierre", 16, "Première"),
    Personnel("Julie", 35, "Professeur"),
]

# Polymorphisme en action : même méthode appelée, comportement différent selon l'objet
for p in personnes:
    p.se_presenter()  # Appelle la version spécifique à la classe (Eleve ou Personnel)
