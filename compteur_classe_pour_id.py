class Reservation:
    compteur = 0
    def __init__(self, nom, date):
        self.nom = nom
        self.date = date
        Reservation.compteur += 1
        self.id = Reservation.compteur
        
    def afficher(self):
        print(f"Réservation {self.id}: {self.nom} le {self.date}")
        
        
    
    
resa_1 = Reservation("Jean", "2023-10-01")
resa_1.afficher()
resa_2 = Reservation("Marie", "2023-10-02")
resa_2.afficher()
resa_3 = Reservation("Pierre", "2023-10-03")
resa_3.afficher()
print(Reservation.compteur)


