# ---------------------------
# Fonctions
# ---------------------------

def clear_console():
    print("\n" * 50)

def afficher_menu():
    print("Bonjour, application de gestion des paniers")
    print("1. Choix 1")
    print("2. Choix 2")
    print("3. Choix 3")
    print("q. Quitter")



# -----------------------
# Programme principal
# -----------------------

if __name__ == "__main__":
    while True:
        clear_console()
        afficher_menu()
        choix = input("Faites votre choix : ").strip().lower()
        
        if choix == "1":
            clear_console()
            print("Vous avez choisi l'option 1.")
            input("Appuyez sur Entrée pour revenir au menu...")
            
        elif choix == "2":
            clear_console()
            print("Vous avez choisi l'option 2.")
            input("Appuyez sur Entrée pour revenir au menu...")
            
        elif choix == "3":
            clear_console()
            print("Vous avez choisi l'option 3.")
            input("Appuyez sur Entrée pour revenir au menu...")
            
        elif choix == "q":
            clear_console()
            print("Au revoir !")
            break
        
        else:
            print("Choix invalide.")
            input("Appuyez sur Entrée pour réessayer...")
