# L'exercice Panier/articles est un problème complexe que l'on découpe en plusieurs sous-problèmes :
# - Créer une classe Article
# - Créer une méthode pour calculer le total d'un article
# - Créer une méthode pour afficher les attributs d'un article
# - Créer une classe Panier
# - Créer une méthode pour ajouter un article au panier
# - Créer une méthode pour afficher le contenu du panier

class Article:
    def __init__(self, nom, prix, quantite):
        self.nom = nom
        self.prix = prix
        self.quantite = quantite
        
    def total(self):
        self.total = self.prix * self.quantite
        return self.total
        
    def afficher(self):
        print(f"Nom: {self.nom}, Prix: {self.prix}, Quantité: {self.quantite}, Total: {self.total()}")
        
# Tout de suite après avoir écrite un classe, une méthode ou autre, LE.LA TESTER immédiatemment !

# Série de tests pour la classe Article en cours de développement :
# On teste déjà si l'innitialisation fonctionne:
article_1 = Article('Pantoufle GUCCI', 400, 7)
article_2 = Article('Kinder Bueno', 2.24, 5)
# Si absence de message d'erreur, c'est ok. (Rien ne s'affiche car on n'a rien demandé d'afficher pour l'instant)

# Maintenant testions l'affichage des attributs :
print("nom de l'article 1", article_1.nom)
print("prix de l'article 1", article_1.prix)

# Test de la méthode d'affichage:
article_2.afficher()

# On a fini et testé la classe Article, on s'occupe maintenant de la classe Panier:

class Panier:
    def __init__(self):
        self.articles = [] # liste d'articles vide, que l'on va remplir avec des méthodes

    def ajouter_article(self, article):
        self.articles.append(article)
        
    def afficher_panier(self):
        # afficher une ligne par article, en utilisant une boucle for
        for article in self.articles:
            article.afficher()
        
   
# on teste direct :
panier_1 = Panier()
panier_1.ajouter_article(article_1)
panier_1.ajouter_article(article_2)
panier_1.afficher_panier()

# Ensuite, ajouter les autres méthodes de la classe panier, et les tester:
#     def retirer_article(self, article):
#         self.articles.remove(article)
        
#     def modifier_quantite_article(self, article, quantite):
#         article.quantite = quantite
        
#     def total_panier(self):
#         ...
    
#     def afficher_contenu(self):
#         ...
        
    