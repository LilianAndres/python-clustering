class Maillon:

    def __init__(self, p, precedent, suivant):
        self.p = p
        self.precedent = precedent
        self.suivant = suivant
        self.voisins = []

    