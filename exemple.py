class Rectangle:
    def __init__(self, largeur, longueur):
        self.largeur = largeur
        self.longueur = longueur
        
    def afficher(self):
        print(f"Largeur: {self.largeur}, Longueur: {self.longueur}")
        
    def surface(self):
        return self.largeur * self.longueur
    
    def perimetre(self):
        return 2 * (self.largeur + self.longueur)
        

rectangle_1 = Rectangle(5, 10)
rectangle_2 = Rectangle(7, 14)

rectangle_1.afficher()
rectangle_2.afficher()

print(f"Surface du rectangle 1: {rectangle_1.surface()}")
print(f"Périmètre du rectangle 2: {rectangle_2.perimetre()}")

rectangle_2.largeur = 8

rectangle_2.afficher()