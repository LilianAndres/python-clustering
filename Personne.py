from itertools import count
from multiprocessing import set_forkserver_preload

from numpy import char


class Personne:
    
    _id = count(0)

    def __init__(self, metriques):
        # identification
        self.id = next(self._id)
        self.metriques = metriques 


    def getMetriquesByPoids(self, poids):
        """Renvoie le sous-tableau des métriques de priorité donnée"""
        tab = []
        for i in range(len(self.metriques)):
            if self.metriques[i].poids == poids:
                tab.append(self.metriques[i])

        # erreur si la priorite spécifié n'existe pas dans les métriques
        if len(tab) == 0:
            return None
        
        return tab

    
    def getTousLesPoids(self):
        """Renvoie le tableau des poids dans l'ordre croissant"""
        tab = []
        for i in range(len(self.metriques)):
            if self.metriques[i].poids not in tab:
                tab.append(self.metriques[i].poids)
        
        tab = tab.sort()  

        return tab


    def Comparer(self, p):
        """Compare deux personnes en fonction de leurs métriques et de leurs sous-métriques"""

        tauxCompatibilite = 0
        poidsTotal = 0

        for i in range(len(self.metriques)):
            poidsTotal += self.metriques[i].poids
            if self.metriques[i].valeur == p.metriques[i].valeur:
                tauxCompatibilite += self.metriques[i].poids

        return (tauxCompatibilite / poidsTotal)


        

