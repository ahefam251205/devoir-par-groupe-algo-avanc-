# Partie 1 - Début du projet : définition de la structure de l'arbre

class Noeud:
    def __init__(self, valeur):
        self.valeur = valeur
        self.gauche = None
        self.droite = None

    def __repr__(self):
        return f"Noeud({self.valeur})"


class ABR:
    def __init__(self):
        self.racine = None

    def inserer(self, valeur):
        # fonction vide pour l'instant, sera complétée par le prochain membre
        pass

    def est_vide(self):
        """Retourne True si l'arbre est vide"""
        return self.racine is None
