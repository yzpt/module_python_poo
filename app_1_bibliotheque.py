class Livre:
    def __init__(self, titre, ISBN, auteur, disponibilite):
        self.titre = titre
        self.auteur = auteur
        
    def afficher(self):
        print(f"Titre: {self.titre}, Auteur: {self.auteur}")
        
# -----------------------
# Interface utilisateur
# -----------------------

def clear_console():
    print("\n" * 50)

def afficher_menu():
    print("Bienvenue dans la bibliothèque")
    print("1. Afficher tous les livres")
    print("2. Ajouter un livre")
    print("q. Quitter")


# -----------------------
# Programme principal
# -----------------------

if __name__ == "__main__":
    
    # On crée une liste de livres vide
    livres = []
    
    # Ajout de quelques livres
    livre1 = Livre("Le Petit Prince", "978-3-16-148410-0", "Antoine de Saint-Exupéry", True)
    livre2 = Livre("1984", "978-0-452-28423-4", "George Orwell", False)
    
    livres.append(livre1)
    livres.append(livre2)
    
    while True:
        clear_console()
        afficher_menu()
        choix = input("Faites votre choix : ").strip().lower()
        
        if choix == "1":
            clear_console()
            print("Liste des livres :")
            print("------------------------")
            for livre in livres:
                livre.afficher()
            print("------------------------")
            input("Appuyez sur Entrée pour revenir au menu...")
            
        elif choix == "2":
            ...
        
        elif choix == "q":
            clear_console()
            print("Au revoir !")
            break
        
        else:
            print("Choix invalide.")
            input("Appuyez sur Entrée pour réessayer...")
        
