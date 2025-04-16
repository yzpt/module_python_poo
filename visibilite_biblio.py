# Visibilité des attributs et méthodes en Python (exemple : gestion de bibliothèque)

# ┌────────────┬───────────┬────────────────────┬────────────────────────────────────────────────────┐
# │  Niveau    │ Préfixe   │ Accès extérieur    │ Usage recommandé                                   │
# ├────────────┼───────────┼────────────────────┼────────────────────────────────────────────────────┤
# │ Public     │ nom       │ Oui                │ Interface prévue pour être utilisée de l’extérieur │
# ├────────────┼───────────┼────────────────────┼────────────────────────────────────────────────────┤
# │ Protégé    │ _nom      │ Oui (déconseillé)  │ Usage interne ou en héritage uniquement            │
# ├────────────┼───────────┼────────────────────┼────────────────────────────────────────────────────┤
# │ Privé      │ __nom     │ Non                │ Strictement réservé à l’intérieur de la classe     │
# └────────────┴───────────┴────────────────────┴────────────────────────────────────────────────────┘


class Livre:
    def __init__(self, titre, total_exemplaires):
        # ✅ Attribut public : consultable librement
        self.titre = titre

        # ⚠️ Attribut protégé : réservé à l'usage interne
        self._historique_emprunts = []

        # 🔒 Attribut privé : nombre d'exemplaires disponibles
        self.__exemplaires_disponibles = total_exemplaires

    # ✅ Méthode publique : permet d’emprunter un livre
    def emprunter(self, nom_lecteur):
        if self.__exemplaires_disponibles > 0:
            self.__exemplaires_disponibles -= 1
            self.__enregistrer_emprunt(f"{nom_lecteur} a emprunté le livre.")
        else:
            print("❌ Aucun exemplaire disponible pour emprunt.")

    # ✅ Méthode publique : permet de retourner un livre
    def retourner(self, nom_lecteur):
        self.__exemplaires_disponibles += 1
        self.__enregistrer_emprunt(f"{nom_lecteur} a retourné le livre.")

    # ✅ Méthode publique : affiche le nombre d’exemplaires disponibles
    def afficher_disponibilite(self):
        print(f"📚 Disponibilité du livre « {self.titre} » : {self.__exemplaires_disponibles} exemplaire(s)")

    # ✅ Méthode publique : affiche l’historique des emprunts/retours
    def afficher_historique(self):
        print("📄 Historique des emprunts :")
        for ligne in self._historique_emprunts:
            print("-", ligne)

    # 🔒 Méthode privée : enregistre une opération d’emprunt/retour
    def __enregistrer_emprunt(self, texte):
        self._historique_emprunts.append(texte)


# --- Utilisation concrète ---

livre = Livre("1984", 3)

livre.emprunter("Alice")            # ✅ Méthode publique
livre.emprunter("Bob")
livre.retourner("Alice")            # ✅ Méthode publique
livre.afficher_disponibilite()      # ✅ Méthode publique
livre.afficher_historique()         # ✅ Méthode publique

# --- Accès aux attributs ---

print(livre.titre)                  # ✅ Attribut public
print(livre._historique_emprunts)  # ⚠️ Attribut protégé
# print(livre.__exemplaires_disponibles)  # ❌ Erreur : attribut privé
# livre.__enregistrer_emprunt("Test")    # ❌ Erreur : méthode privée
