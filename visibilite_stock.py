# Visibilité des attributs et méthodes en Python (exemple : gestion de stock)

# ┌────────────┬───────────┬────────────────────┬────────────────────────────────────────────────────┐
# │  Niveau    │ Préfixe   │ Accès extérieur    │ Usage recommandé                                   │
# ├────────────┼───────────┼────────────────────┼────────────────────────────────────────────────────┤
# │ Public     │ nom       │ Oui                │ Interface prévue pour être utilisée de l’extérieur │
# ├────────────┼───────────┼────────────────────┼────────────────────────────────────────────────────┤
# │ Protégé    │ _nom      │ Oui (déconseillé)  │ Usage interne ou en héritage uniquement            │
# ├────────────┼───────────┼────────────────────┼────────────────────────────────────────────────────┤
# │ Privé      │ __nom     │ Non                │ Strictement réservé à l’intérieur de la classe     │
# └────────────┴───────────┴────────────────────┴────────────────────────────────────────────────────┘


class Produit:
    def __init__(self, nom, stock_initial):
        # ✅ Attribut public : accessible directement
        self.nom = nom

        # ⚠️ Attribut protégé : réservé à un usage interne
        self._mouvements_stock = []

        # 🔒 Attribut privé : stock réel, inaccessible directement de l’extérieur
        self.__stock = stock_initial

    # ✅ Méthode publique : permet d'ajouter du stock
    def approvisionner(self, quantite):
        if self._valider_quantite(quantite):
            self.__stock += quantite
            self.__enregistrer_mouvement(f"Approvisionnement : +{quantite} unités")

    # ✅ Méthode publique : permet de retirer du stock
    def retirer_stock(self, quantite):
        if self._valider_quantite(quantite) and self.__stock >= quantite:
            self.__stock -= quantite
            self.__enregistrer_mouvement(f"Retrait : -{quantite} unités")
        else:
            print("❌ Retrait impossible : stock insuffisant ou quantité invalide")

    # ✅ Méthode publique : affiche le stock disponible
    def afficher_stock(self):
        print(f"📦 Stock de {self.nom} : {self.__stock} unités")

    # ✅ Méthode publique : affiche l’historique des mouvements
    def afficher_mouvements(self):
        print("📄 Historique des mouvements de stock :")
        for mouvement in self._mouvements_stock:
            print("-", mouvement)

    # ⚠️ Méthode protégée : vérifie si la quantité est valide
    def _valider_quantite(self, quantite):
        return isinstance(quantite, int) and quantite > 0

    # 🔒 Méthode privée : enregistre un mouvement dans l'historique
    def __enregistrer_mouvement(self, description):
        self._mouvements_stock.append(description)


# --- Utilisation concrète ---

produit = Produit("Batteries lithium", 100)

produit.approvisionner(50)         # ✅ Méthode publique
produit.retirer_stock(30)          # ✅ Méthode publique
produit.afficher_stock()           # ✅ Méthode publique
produit.afficher_mouvements()      # ✅ Méthode publique

# --- Accès aux attributs ---

print(produit.nom)                 # ✅ Attribut public
print(produit._mouvements_stock)  # ⚠️ Attribut protégé
# print(produit.__stock)          # ❌ Erreur : attribut privé
# produit.__enregistrer_mouvement("Test")  # ❌ Erreur : méthode privée
