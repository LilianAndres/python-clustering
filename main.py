import os
import numpy as np
import pandas
from Maillon import Maillon
from Graphe import Graphe
from Metrique import Metrique
from Personne import Personne
from Struct import Struct

def main():
    
    # entry point
    dataset = pandas.read_csv("dataset.csv")

    # normalisation des données
    dataset.drop(dataset.columns[[0,2,5,6,7,8,10,12,14,15,17]], axis=1, inplace=True)
    dataset.rename(columns={
        "Duree du trajet": "temps_trajet",
        "Aimez vous Hole-io ?": "hole_io",
        "Marque téléphone": "telephone",
        "Etes-vous viril (e)": "charismatique",
        "Êtes-vous un gamer ?": "gamer",
        "Avez-vous déjà eu le covid19 ?": "covid",
        "Taille ?": "taille",
        "Longueur de vos cheveux en cm": "longueur_cheveux",
        "Projet Post-DUT": "projet_pro",
        "Avez-vous un stage ?": "stage",
        "Mois de naissance": "mois_naissance",
        "Année de naissance": "annee_naissance",
        "Navigateur web": "navigateur",
        "Etes-vous fils/fille unique ?": "fraternite",
        "Couleur des yeux": "couleur_yeux",
        "Quel système d'exploitation ?": "os",
        "Couleur des cheveux": "couleur_cheveux",
        "Avez-vous le permis de conduire ?": "permis",
        "Qel est votre nom": "nom"
    }, inplace=True)

    # fixer une priorité à chaque métrique
    prioriteLigne = {
        'temps_trajet': 1,
        'hole_io': 1,
        'telephone': 3,
        'charismatique': 5,
        'gamer': 10,
        'covid': 1,
        'taille': 1,
        'longueur_cheveux': 1,
        'projet_pro': 8,
        'stage': 5,
        'mois_naissance': 3,
        'annee_naissance': 6,
        'navigateur': 4,
        'fraternite': 1,
        'couleur_yeux': 1,
        'os': 7,
        'couleur_cheveux': 1,
        'permis': 3,
        'nom': 0
    }

    dataset = dataset.append(prioriteLigne, ignore_index=True)


    # création de la structure et initialisation des maillons

    struct = Struct()
    
    for i in range(len(dataset)): # pour chaque ligne
        tabMetriques = []
        for j in range(len(dataset.columns.values.tolist())): # pour chaque colonne
            m = Metrique(
                dataset.columns.values.tolist()[j], # nom
                dataset[dataset.columns.values.tolist()[j]].iloc[i], # valeur
                dataset[dataset.columns.values.tolist()[j]].iloc[-1]  # poids
            )
            tabMetriques.append(m)

        p = Personne(tabMetriques)
        struct.Ajouter(p)   


    # struct.Afficher()
 
    ptr = struct.tete

    seuil = 0.5

    # remplir les voisins dans chaque maillon (liste des personnes incompatibles)
    while ptr.suivant != None:
        ptr2 = struct.tete
        while ptr2.suivant != None:
            if ptr.p.Comparer(ptr2.p) < seuil:
                ptr.voisins.append(ptr2.p)
            ptr2 = ptr2.suivant
        ptr = ptr.suivant
        

    # initialise le graphe avec des 0 
    grapheInteraction = np.zeros((len(dataset) - 1, len(dataset) - 1))  

    G = Graphe(grapheInteraction)

    ptr = struct.tete

    # remplir le graphe d'interaction avec les voisins 
    while ptr.suivant != None:
        # pour chaque ligne de la matrice
        for voisin in ptr.voisins:
            grapheInteraction[ptr.p.id][voisin.id] = 1
        ptr = ptr.suivant

    
    # colorer le graphe d'interaction

    # test unitaire avec une matrice 3x3
    a = [
        [0, 0, 1],
        [0, 0, 1],
        [1, 1, 0]
    ]

    colorationA = {2: 1, 0: 2, 1: 2}

    A = Graphe(a)
    
    if A.Coloration() == colorationA:
        print("Coloration de A - success")
    else:
        print("Coloration de A - failed")
    

    # création des clusters à partir de la coloration
    g = G.Coloration()

    clusters = []

    for couleur in list(set(g.values())):
        # on itère pour chaque couleur différente de la coloration
        clusters.append([k for k,v in g.items() if v == couleur])
    
    ptr = struct.tete

    for i in range(len(clusters)):
        print("Cluster " + str(i) + ": " + str(clusters[i]))



if __name__ == "__main__":
    main()