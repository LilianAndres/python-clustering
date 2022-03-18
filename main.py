import numpy as np
import pandas
from Maillon import Maillon
from Personne import Personne
from Struct import Struct

def main():
    
    dataset = pandas.read_csv("dataset.csv")
    
    struct = Struct()

    # initialise le graphe avec des 0 
    grapheInteraction = np.zeros((len(dataset), len(dataset))) 

   # créer la structure avec tous les maillons
    for i in range(len(dataset)):
        personne = Personne(dataset.iloc[i, 29], dataset.iloc[i, 4], dataset.iloc[i, 3], dataset.iloc[i, 12],
        dataset.iloc[i, 16], dataset.iloc[i, 19], dataset.iloc[i, 20], dataset.iloc[i, 21], dataset.iloc[i, 27])
        struct.Ajouter(personne)

    
    ptr = struct.tete

    # remplir les voisins dans chaque maillon (liste des personnes incompatibles)
    while ptr.suivant != None:
        ptr2 = struct.tete
        while ptr2.suivant != None:
            if ptr.p.Comparer(ptr2.p) == False:
                ptr.voisins.append(ptr2.p)
            ptr2 = ptr2.suivant
        ptr = ptr.suivant
        
    ptr = struct.tete

    # remplir le graphe d'interaction avec les voisins 
    while ptr.suivant != None:
        # pour chaque ligne de la matrice
        for voisin in ptr.voisins:
            grapheInteraction[ptr.p.id][voisin.id] = 1
        ptr = ptr.suivant

    
    # colorer le graphe d'interaction

if __name__ == "__main__":
    main()