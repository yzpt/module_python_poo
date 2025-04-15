import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur  # exemple : "As", "Roi", "7"
        self.couleur = couleur  # exemple : "Coeur", "Pique"

    def afficher(self):
        print(f"Carte : {self.valeur} de {self.couleur}")

class Paquet:
    def __init__(self):
        self.cartes = []  # liste de cartes vide

    def ajouter_carte(self, carte):
        self.cartes.append(carte)
        print(f"Carte ajoutée : {carte.valeur} de {carte.couleur}")
        input("Appuyez sur Entrée pour continuer...")
        
    def afficher_cartes(self):
        clear_console()
        print("Liste des cartes :")
        for carte in self.cartes:
            carte.afficher()
        input("Appuyez sur Entrée pour revenir au menu...")

# ---------------------
# Interface application
# ---------------------

def clear_console():
    print("\n" * 50)

def afficher_menu():
    print("Bienvenue dans votre collection de cartes")
    print("1. Afficher toutes les cartes du paquet")
    print("2. Ajouter une carte")
    
    print("q. Quitter")


if __name__ == "__main__":

    paquet = Paquet()

    # Quelques exemples de cartes
    paquet.ajouter_carte(Carte("As", "Coeur"))
    paquet.ajouter_carte(Carte("Roi", "Pique"))
    paquet.ajouter_carte(Carte("7", "Trèfle"))
    paquet.ajouter_carte(Carte("Dame", "Carreau"))

    while True:
        clear_console()
        afficher_menu()
        choix = input("Faites votre choix : ").strip().lower()
        
        if choix == "1":
            # Afficher toutes les cartes
            paquet.afficher_cartes()
        
        elif choix == "2":
            # Ajouter une carte
            valeur = input("Entrez la valeur de la carte : ")
            couleur = input("Entrez la couleur de la carte : ")
            nouvelle_carte = Carte(valeur, couleur)
            paquet.ajouter_carte(nouvelle_carte)                        
            
        elif choix == "q":
            clear_console()
            print("À bientôt !")
            break
        
        else:
            print("Choix invalide.")
            input("Appuyez sur Entrée pour réessayer...")
