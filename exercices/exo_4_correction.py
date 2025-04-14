class Carte:
    def __init__(self, valeur, symbole):
        self.valeur = valeur
        self.symbole = symbole
        
    def afficher(self):
        print(f"{self.valeur} de {self.symbole}")


ma_premiere_carte = Carte('As', 'Coeur')
ma_deuxieme_carte = Carte('Roi', 'Pique')

ma_premiere_carte.afficher()
ma_deuxieme_carte.afficher()

class Paquet:
    def __init__(self):
        self.cartes = []
        
    def ajouter_carte(self, carte):
        self.cartes.append(carte)