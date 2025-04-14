class Compte:
    def __init__(self, nom, solde=0):
        self.nom = nom
        self.solde = solde

    def deposer(self, montant):
        self.solde += montant
        print(f"{montant} a été déposé sur le compte de {self.nom}. Nouveau solde : {self.solde}")

    def retirer(self, montant):
        self.solde -= montant
        print(f"{montant} a été retiré du compte de {self.nom}. Nouveau solde : {self.solde}")
        
    def afficher_solde(self):
        print(f"Solde du compte de {self.nom} : {self.solde}")

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
    
def choix_1(comptes): # On place la variable comptes car on va l'utiliser dans la fonction pour ajouter un compte
    """
    Créer un compte : Ajoute un compte à la liste des comptes
    """
    clear_console()
    print("Création d'un compte")
    nom = input("Nom du titulaire : ")
    solde = float(input("Solde initial (€) : "))
    nouveau_compte = Compte(nom, solde)
    comptes.append(nouveau_compte)
    print(f"Compte créé pour {nom} avec un solde de {solde}€.")
    input("Appuyez sur Entrée pour revenir au menu...")
    
def choix_2(comptes):
    """
    Afficher le solde d'un compte : Affiche le solde d'un compte spécifique
    """
    ...
    
def choix_3(comptes):
    ...
    
def choix_4(comptes):
    ...

def choix_5(comptes):
    ...

if __name__ == "__main__":
    compte1 = Compte("Alice", 1000)
    compte2 = Compte("Bob", 500)
    comptes = [compte1, compte2]
    
    while True:
        clear_console()
        afficher_menu()
        choix = input("Choisissez une option : ")
        
        if choix == "1":
            choix_1(comptes)
        elif choix == "2":
            choix_2(comptes)
        elif choix == "3":
            choix_3(comptes)
        elif choix == "4":
            choix_4(comptes)
        elif choix == "5":
            choix_5(comptes)
        elif choix.lower() == "q":
            print("Merci d'avoir utilisé l'application de gestion des comptes bancaires.")
            break
        else:
            print("Choix invalide, veuillez réessayer.")