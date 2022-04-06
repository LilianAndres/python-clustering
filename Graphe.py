from itertools import count


class Graphe:

    def __init__(self, matrice):
        self.matrice = matrice
    
    
    def TransformeEnDictionnaire(self):
        """Transforme la matrice d'adjacence en un dictionnaire de la forme {sommet: [voisins] ...}"""
        graphe = {}
        for ligne in range(len(self.matrice)):
            liste = []
            for colonne in range(len(self.matrice)):
                if self.matrice[ligne][colonne] == 1:
                    liste.append(colonne)
                graphe[ligne] = liste
        return graphe


    def Coloration(self):
        
        # ordonner les sommets par ordre décroissant 
        graphe = self.TransformeEnDictionnaire()
        sommets = sorted(list(graphe.keys()), key=lambda item: len(graphe[item]), reverse=True)

        # récupérer tous les sommets et initialiser les valeurs
        liste = list(graphe.keys())
        coloration = {}
        couleurActuelle = 1

        # pour chaque sommets, 
        for sommet in sommets:
            # si le sommet n'est pas encore coloré, on le colorie
            if sommet not in coloration:
                coloration[sommet] = couleurActuelle
            
            # et pour chaque sommets,
            for sommet2 in liste:
                # si ce sommet n'est pas voisin de celui qu'on traite et qu'il n'est pas coloré, on colorie
                if sommet2 not in graphe[sommet] and sommet2 not in coloration:
                    coloration[sommet2] = couleurActuelle
            
            # une fois les traitements gérés, on augmente la couleur et on réitère
            if couleurActuelle in coloration.values():
                couleurActuelle += 1

        return coloration