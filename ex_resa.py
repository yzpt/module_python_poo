class Reservation:
    compteur = 0
    def __init__(self, nom, date):
        self.nom = nom
        self.date = date
        Reservation.compteur += 1
        self.id = Reservation.compteur
        
    # Mauvaise pratique, on le faisait par souci pédagogique
    
    # def afficher(self):
    #     print(f"Réservation {self.id}: {self.nom} le {self.date}")
    
    # Bonne pratique : utiliser __str__ pour afficher l'objet
    def __str__(self):
        return f"Réservation {self.id}: {self.nom} le {self.date}"  
        
resa_1 = Reservation("Jean", "2023-10-01")
resa_2 = Reservation("Marie", "2023-10-02")
resa_3 = Reservation("Pierre", "2023-10-03")

# resa_1.afficher()
print(resa_1)
