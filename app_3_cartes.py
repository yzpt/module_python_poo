import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur  # exemple : "As", "Roi", "7"
        self.couleur = couleur  # exemple : "Coeur", "Pique"

    def afficher(self):
        print(f"Carte : {self.valeur} de {self.couleur}")
    


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

    cartes = [] #paquet de cartes vide

    # Quelques exemples de cartes
    cartes.append(Carte("As", "Coeur"))
    cartes.append(Carte("Roi", "Pique"))
    cartes.append(Carte("7", "Trèfle"))
    cartes.append(Carte("Dame", "Carreau"))

    while True:
        clear_console()
        afficher_menu()
        choix = input("Faites votre choix : ").strip().lower()
        
        if choix == "1":
            # Afficher toutes les cartes
            clear_console()
            print("Liste des cartes :")
            for carte in cartes:
                carte.afficher()
            input("Appuyez sur Entrée pour revenir au menu...")
            
        elif choix == "2":
            ...
            
        elif choix == "3":
            # Mélanger les cartes
            clear_console()
            random.shuffle(cartes)
            print("Les cartes ont été mélangées.")
            input("Appuyez sur Entrée pour revenir au menu...")
            
        
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
