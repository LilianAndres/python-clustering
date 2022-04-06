class Metrique:

    def __init__(self, nom, valeur, poids=1):
        """Si le jeu de données est petit, on peut spécifier des poids manuels, sinon ils valent tous 1."""
        self.nom = nom
        self.valeur = valeur
        if poids == 1:
            self.poids = 1
        else:
            self.poids = poids
