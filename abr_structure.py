# Partie 1 - Début du projet : définition de la structure de l'arbre

class Noeud:
    def __init__(self, valeur):
        self.valeur = valeur
        self.gauche = None
        self.droite = None

class ABR:
    def __init__(self):
        self.racine = None

    def inserer(self, valeur):
        # fonction vide pour l'instant, sera complétée par le prochain membre
        pass
   def est_vide(self):
        """Retourne True si l'arbre est vide"""
        return self.racine is None


# ===== Partie 3 : recherche, parcours et programme principal =====

# Méthodes complètes d'insertion et de recherche
class ABR:
    def __init__(self):
        self.racine = None

    def inserer(self, valeur):
        if self.racine is None:
            self.racine = Noeud(valeur)
        else:
            self._inserer(self.racine, valeur)

    def _inserer(self, noeud, valeur):
        if valeur < noeud.valeur:
            if noeud.gauche is None:
                noeud.gauche = Noeud(valeur)
            else:
                self._inserer(noeud.gauche, valeur)
        else:
            if noeud.droite is None:
                noeud.droite = Noeud(valeur)
            else:
                self._inserer(noeud.droite, valeur)

    def rechercher(self, valeur):
        return self._rechercher(self.racine, valeur)

    def _rechercher(self, noeud, valeur):
        if noeud is None:
            return False
        if noeud.valeur == valeur:
            return True
        elif valeur < noeud.valeur:
            return self._rechercher(noeud.gauche, valeur)
        else:
            return self._rechercher(noeud.droite, valeur)

    def parcours_infixe(self, noeud):
        if noeud is not None:
            self.parcours_infixe(noeud.gauche)
            print(noeud.valeur, end=" ")
            self.parcours_infixe(noeud.droite)


# ==== Programme principal ====
if __name__ == "__main__":
    arbre = ABR()

    valeurs = [10, 5, 20, 3, 7, 15]
    for v in valeurs:
        arbre.inserer(v)

    print("Parcours infixe :")
    arbre.parcours_infixe(arbre.racine)

    print("\nRecherche 7 :", arbre.rechercher(7))
    print("Recherche 100 :", arbre.rechercher(100))
