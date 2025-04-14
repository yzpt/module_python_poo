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
        ...
        
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

