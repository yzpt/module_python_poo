class Compte:
    def __init__(self, nom, solde=0):
        self.nom = nom
        self.solde = solde

    def deposer(self, montant):
        self.solde += montant
        print(f"{montant} a été déposé sur le compte de {self.nom}. Nouveau solde : {self.solde}")
        
    def retirer(self, montant):
        ...
        
    def afficher_solde(self):
        print(f"Le solde du compte de {self.nom} est de {self.solde}€.")
        
        
# -----------------------
# Interface utilisateur
# -----------------------

def clear_console():
    print("\n" * 50)

def afficher_menu():
    print("Bonjour, application de gestion des comptes bancaires")
    print("1. Créer un compte")
    print("2. Afficher le solde d'un compte")
    print("3. Déposer de l'argent")
    print("4. Retirer de l'argent")
    print("5. Afficher tous les comptes")
    print("q. Quitter")
    

if __name__ == "__main__":
    # Données initiales
    compte1 = Compte("Alice", 1000)
    compte2 = Compte("Bob", 500)
    compte3 = Compte("Charlie", 200)
    comptes = [compte1, compte2, compte3]
    
    while True:
        clear_console()
        afficher_menu()
        choix = input("Choisissez une option : ")
        
        if choix == "1":
            clear_console()
            print("Création d'un compte")
            nom = input("Nom du titulaire : ")
            solde = float(input("Solde initial (€) : "))
            nouveau_compte = Compte(nom, solde)
            comptes.append(nouveau_compte)
            print(f"Compte créé pour {nom} avec un solde de {solde}€.")
            input("Appuyez sur Entrée pour revenir au menu...")
        
        elif choix == "2":
            clear_console()
            print("Afficher le solde d'un compte")
            
            # il faut retrouver le compte correspond au nom tapé par l'utilisateur
            nom = input("Nom du titulaire : ")    
            for compte in comptes:
                if compte.nom.lower() == nom.lower():
                    # on appelle la méthode afficher_solde de la classe Compte (il faut l'écrire !)
                    compte.afficher_solde()
                    input("Appuyez sur Entrée pour revenir au menu...")
                    break
        
        elif choix == "3":
            clear_console()
            print("Déposer de l'argent sur un compte à partir du nom du titulaire") 
            
            # il faut retrouver le compte correspond au nom tapé par l'utilisateur
            nom = input("Nom du titulaire : ")    
            for compte in comptes:
                if compte.nom.lower() == nom.lower():
                    # Là, nous avons retrouvé le compte sur lequel on veut déposer de l'argent
                    # demander le montant à déposer
                    # ajouter ce montant au compte sélectionné
                    ...
            
        elif choix == "4":
            ...
        
        elif choix == "5":
            # afficher tous les comptes
            clear_console()
            print("Liste des comptes :")
            for compte in comptes:
                print(f"{compte.nom} : {compte.solde}€")
            input("Appuyez sur Entrée pour revenir au menu...")

        elif choix.lower() == "q":
            print("Merci d'avoir utilisé l'application de gestion des comptes bancaires.")
            break
        else:
            print("Choix invalide, veuillez réessayer.")