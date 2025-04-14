class Article:
    def __init__(self, id, nom, prix, quantite):
        self.id = id
        self.nom = nom
        self.prix = prix
        self.quantite = quantite
        
    def total(self):
        ...
        
    def __str__(self):
        return f"Article: {self.nom}, Prix: {self.prix}, Quantité: {self.quantite}, Total: {self.total()}"
    

class Panier:
    def __init__(self):
        self.articles = [] # Liste d'articles vide
    
    def ajouter_article(self, article):
        ...
        
    def retirer_article(self, article):
        ...
        
    def modifier_quantite_article(self, article, quantite):
        ...
    
    def vider_panier(self):
        ...
            
    def afficher_contenu(self):
        ...

