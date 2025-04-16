# Visibilité des attributs et méthodes en Python

# ┌────────────┬───────────┬────────────────────┬────────────────────────────────────────────────────┐
# │  Niveau    │ Préfixe   │ Accès extérieur    │ Usage recommandé                                   │
# ├────────────┼───────────┼────────────────────┼────────────────────────────────────────────────────┤
# │ Public     │ nom       │ Oui                │ Interface prévue pour être utilisée de l’extérieur │
# ├────────────┼───────────┼────────────────────┼────────────────────────────────────────────────────┤
# │ Protégé    │ _nom      │ Oui (déconseillé)  │ Usage interne ou en héritage uniquement            │
# ├────────────┼───────────┼────────────────────┼────────────────────────────────────────────────────┤
# │ Privé      │ __nom     │ Non                │ Strictement réservé à l’intérieur de la classe     │
# └────────────┴───────────┴────────────────────┴────────────────────────────────────────────────────┘


class CompteBancaire:
    def __init__(self, titulaire, solde_initial):
        # ✅ Attribut public : accessible directement depuis l'extérieur
        self.titulaire = titulaire

        # ⚠️ Attribut protégé : par convention, réservé à un usage interne ou par héritage
        self._historique = []

        # 🔒 Attribut privé : ne doit pas être accédé ni modifié depuis l'extérieur
        self.__solde = solde_initial

    # ✅ Méthode publique : peut être appelée de l'extérieur
    def deposer(self, montant):
        if self._valider_montant(montant):  # utilisation d'une méthode protégée
            self.__solde += montant
            self.__enregistrer_operation(f"Dépôt : +{montant}€")  # utilisation d'une méthode privée

    # ✅ Méthode publique : peut être appelée de l'extérieur
    def retirer(self, montant):
        if self._valider_montant(montant) and self.__solde >= montant:
            self.__solde -= montant
            self.__enregistrer_operation(f"Retrait : -{montant}€")
        else:
            print("❌ Retrait impossible : solde insuffisant ou montant invalide")

    # ✅ Méthode publique : permet d'afficher le solde
    def afficher_solde(self):
        print(f"💰 Solde de {self.titulaire} : {self.__solde}€")

    # ✅ Méthode publique : affiche les opérations enregistrées
    def afficher_historique(self):
        print("📄 Historique des opérations :")
        for ligne in self._historique:
            print("-", ligne)

    # ⚠️ Méthode protégée : destinée à un usage interne ou par héritage
    def _valider_montant(self, montant):
        return isinstance(montant, (int, float)) and montant > 0

    # 🔒 Méthode privée : utilisée uniquement en interne dans la classe
    def __enregistrer_operation(self, texte):
        self._historique.append(texte)


# --- Utilisation concrète ---

compte = CompteBancaire("Toto", 500)

compte.deposer(150)         # ✅ Appel d'une méthode publique
compte.retirer(50)          # ✅ Appel d'une méthode publique
compte.afficher_solde()     # ✅ Appel d'une méthode publique
compte.afficher_historique()

# --- Accès aux attributs ---

print(compte.titulaire)         # ✅ Attribut public
print(compte._historique)       # ⚠️ Attribut protégé (accessible mais déconseillé)
# print(compte.__solde)         # ❌ Erreur : attribut privé
# compte.__enregistrer_operation("Test")  # ❌ Erreur : méthode privée


