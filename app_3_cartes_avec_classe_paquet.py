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
        ...

    def melanger(self):
        ...

    def tirer_carte(self):
        ...

    def retirer_carte(self, carte):
        ...

    def vider_paquet(self):
        ...


def clear_console():
    print("\n" * 50)

def afficher_menu():
    print("Bienvenue dans votre collection de cartes")
    print("1. Afficher toutes les cartes qu paquet")
    print("2. Ajouter une carte")
    print("3. Mélanger les cartes")
    print("4. Tirer une carte du paquet, l'afficher, la remettre") # attention à vérifier si le paquet est vide !
    print("5. Retirer une carte du paquet") # attention à vérifier si le paquet est vide !
    print("6. Vider le paquet")
    
    print("7. Ajouter automatiquement les 52 cartes à jouer dans paquet") 
    # option7: facultatif mais très intéressant : il faut imbriquer 2 boucles for.
    # valeurs = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi", "As"]
    # couleurs = ["Coeur", "Pique", "Trèfle", "Carreau"]
    # ... que faire ensuite ?
    
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
            ...
            
        elif choix == "2":
            valeur = input("Entrez la valeur de la carte : ")
            couleur = input("Entrez la couleur de la carte : ")
            nouvelle_carte = Carte(valeur, couleur)
            paquet.ajouter_carte(nouvelle_carte)
            
        elif choix == "3":
            ...
        
        elif choix == "4":
            ...
            
        elif choix == '5':
            ...
                        
        elif choix == "q":
            clear_console()
            print("À bientôt !")
            break
        
        else:
            print("Choix invalide.")
            input("Appuyez sur Entrée pour réessayer...")
