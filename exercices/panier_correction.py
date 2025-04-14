class Article:
    def __init__(self, nom, prix, quantite):
        self.nom = nom
        self.prix = prix
        self.quantite = quantite

    def total(self):
        return self.prix * self.quantite

    def afficher(self):
        print(f"Nom: {self.nom}, Prix: {self.prix}€, Quantité: {self.quantite}, Total: {self.total():.2f}€")


# Tests de la classe Article
article_1 = Article('Pantoufle GUCCI', 400, 7)
article_2 = Article('Kinder Bueno', 2.24, 5)

print("nom de l'article 1", article_1.nom)
print("prix de l'article 1", article_1.prix)

article_2.afficher()


class Panier:
    def __init__(self):
        self.articles = []  # Liste vide d'articles

    def ajouter_article(self, article):
        self.articles.append(article)

    def retirer_article(self, article):
        if article in self.articles:
            self.articles.remove(article)
        else:
            print("Article non trouvé dans le panier.")

    def modifier_quantite_article(self, nom_article, nouvelle_quantite):
        for article in self.articles:
            if article.nom == nom_article:
                article.quantite = nouvelle_quantite
                print(f"Quantité de '{nom_article}' mise à jour à {nouvelle_quantite}")
                return
        print(f"Article '{nom_article}' non trouvé dans le panier.")

    def total_panier(self):
        total = sum(article.total() for article in self.articles)
        return total

    def afficher_panier(self):
        if not self.articles:
            print("Le panier est vide.")
        else:
            print("Contenu du panier :")
            for article in self.articles:
                article.afficher()
            print(f"Total général du panier : {self.total_panier():.2f}€")


# Tests de la classe Panier
panier_1 = Panier()
panier_1.ajouter_article(article_1)
panier_1.ajouter_article(article_2)
panier_1.afficher_panier()

# Test modification de quantité
panier_1.modifier_quantite_article('Kinder Bueno', 10)
panier_1.afficher_panier()

# Test suppression
panier_1.retirer_article(article_1)
panier_1.afficher_panier()

# Test total seul
print("Total final du panier :", panier_1.total_panier(), "€")
