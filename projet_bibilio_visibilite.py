class Livre:
    def __init__(self, titre, auteur, exemplaires):
        self.titre = titre                        # ✅ public
        self.auteur = auteur                      # ✅ public
        self._code_interne = f"{titre[:3]}-{auteur[:3]}"  # ⚠️ protégé
        self.__exemplaires = exemplaires          # 🔒 privé

    def est_disponible(self):
        return self.__exemplaires > 0             # ✅ méthode publique

    def emprunter(self):
        if self.__exemplaires > 0:
            self.__exemplaires -= 1
            return True
        return False

    def retourner(self):
        self.__exemplaires += 1

    def afficher_disponibilite(self):
        print(f"📖 {self.titre} - {self.auteur} : {self.__exemplaires} exemplaire(s) dispo.")

    def _get_code(self):                          # ⚠️ méthode protégée
        return self._code_interne

    def __str__(self):
        return f"{self.titre} de {self.auteur}"


class Lecteur:
    def __init__(self, nom):
        self.nom = nom                            # ✅ public
        self._historique = []                     # ⚠️ protégé
        self.__emprunts = []                      # 🔒 privé

    def emprunter(self, livre):
        if livre.emprunter():
            self.__emprunts.append(livre)
            self._historique.append(f"✔️ Emprunté : {livre}")
        else:
            print(f"❌ {livre} non disponible")

    def retourner(self, livre):
        if livre in self.__emprunts:
            livre.retourner()
            self.__emprunts.remove(livre)
            self._historique.append(f"↩️ Retourné : {livre}")

    def afficher_historique(self):
        print(f"📚 Historique de {self.nom} :")
        for action in self._historique:
            print("-", action)

    def lister_emprunts(self):
        print(f"📦 Livres empruntés par {self.nom} :")
        for livre in self.__emprunts:
            print("-", livre)


class Bibliotheque:
    def __init__(self):
        self.catalogue = []                       # ✅ public

    def ajouter_livre(self, livre):
        self.catalogue.append(livre)

    def afficher_catalogue(self):
        print("📚 Catalogue de la bibliothèque :")
        for livre in self.catalogue:
            livre.afficher_disponibilite()


# --- Utilisation concrète ---

livre1 = Livre("1984", "Orwell", 2)
livre2 = Livre("Le Meilleur des Mondes", "Huxley", 1)

alice = Lecteur("Alice")
bob = Lecteur("Bob")

biblio = Bibliotheque()
biblio.ajouter_livre(livre1)
biblio.ajouter_livre(livre2)

biblio.afficher_catalogue()

alice.emprunter(livre1)
bob.emprunter(livre1)
bob.emprunter(livre2)
bob.emprunter(livre1)  # ❌ plus d'exemplaires

alice.retourner(livre1)
bob.emprunter(livre1)  # ✅ maintenant dispo

print()
alice.afficher_historique()
bob.afficher_historique()

print()
biblio.afficher_catalogue()

