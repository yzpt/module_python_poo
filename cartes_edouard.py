class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur  # exemple : "As", "Roi", "7"
        self.couleur = couleur  # exemple : "Coeur", "Pique"

    def afficher(self):
        print(f"Carte : {self.valeur} de {self.couleur}")
        
    def __eq__(self, value):
        return self.valeur == value.valeur and self.couleur == value.couleur
        
    

cartes = [] #paquet de cartes vide
cartes.append(Carte("As", "Coeur"))
cartes.append(Carte("Roi", "Pique"))
cartes.append(Carte("7", "Trèfle"))
cartes.append(Carte("Dame", "Carreau"))


# valeurs = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi", "As"]
# couleurs = ["Coeur", "Pique", "Trèfle", "Carreau"]
cartes_de_reference = []
for valeur in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi", "As"]:
    for couleur in ["Coeur", "Pique", "Trèfle", "Carreau"]:
        cartes_de_reference.append(Carte(valeur, couleur))

cartes_complementaires = []
for carte in cartes_de_reference:
    carte_ref_valeur = carte.valeur
    carte_ref_couleur = carte.couleur
    
    for carte_a_comparer in cartes:
        if (carte_a_comparer.valeur == carte_ref_valeur) & (carte_a_comparer.couleur == carte_ref_couleur):
            break
    else:
        cartes_complementaires.append(carte)
        
print("Cartes complémentaires :")
for carte in cartes_complementaires:
    carte.afficher()