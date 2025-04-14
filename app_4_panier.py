class Article:
    def __init__(self, nom, prix, quantite):
        self.nom = nom
        self.prix = prix
        self.quantite = quantite

    def total(self):
        return self.prix * self.quantite

    def afficher(self):
        print(f"Nom: {self.nom}, Prix: {self.prix}€, Quantité: {self.quantite}, Total: {self.total():.2f}€")


class Panier:
    def __init__(self):
        self.articles = []

    def ajouter_article(self, article):
        self.articles.append(article)

    def afficher_panier(self):
        print("Contenu du panier :")
        for article in self.articles:
            article.afficher()
    


# -----------------------
# Interface utilisateur
# -----------------------

def clear_console():
    print("\n" * 50)

def afficher_menu():
    print("Bonjour, application de gestion des paniers")
    print("1. Ajouter un article")
    print("2. Afficher le contenu du panier")
    print("q. Quitter")

# Fonctions liées au menu
def choix_1(panier):
    clear_console()
    print("Ajout d'un article")
    nom = input("Nom de l'article : ")
    prix = float(input("Prix de l'article (€) : "))
    quantite = int(input("Quantité : "))
    article = Article(nom, prix, quantite)
    panier.ajouter_article(article)
    print("Article ajouté avec succès.")
    input("Appuyez sur Entrée pour revenir au menu...")

def choix_2(panier):
    clear_console()
    # ... ?
    input("\nAppuyez sur Entrée pour revenir au menu...")


def main():
    panier = Panier()

    while True:
        clear_console()
        afficher_menu()
        choix = input("Faites votre choix : ").strip().lower()
        if choix == "1":
            choix_1(panier)
        elif choix == "2":
            choix_2(panier)
        elif choix == "q":
            clear_console()
            print("Au revoir !")
            break
        else:
            print("Choix invalide.")
            input("Appuyez sur Entrée pour réessayer...")


if __name__ == "__main__":
    main()
