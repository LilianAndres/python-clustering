import os
import numpy as np
import pandas
from Maillon import Maillon
from Personne import Personne
from Struct import Struct

def main():
    
    dataset = pandas.read_csv("dataset.csv")

    # normalisation des données
    dataset.drop(dataset.columns[[2,5,6,7,8,10,12,14,15,17]], axis=1, inplace=True)
    dataset.rename(columns={
        "Duree du trajet": "temps_trajet",
        "Aimez vous Hole-io ?": "hole_io",
        "Marque téléphone": "telephone",
        "Etes-vous viril (e)": "charismatique",
        "Êtes-vous un gamer ?": "gamer",
        "Avez-vous déjà eu le covid19 ?": "covid",
        "Est-ce que Dylan est une mauvaise personne ?": "dylan", # débug !
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

    print(dataset.columns)
    
#     struct = Struct()

#     # initialise le graphe avec des 0 
#     grapheInteraction = np.zeros((len(dataset), len(dataset))) 


#    # créer la structure avec tous les maillons
#     for i in range(len(dataset)):

#         personne = Personne(
#             nom=dataset[['nom']].iloc[i],
#             tempsTrajet=dataset[['temps_trajet']].iloc[i],
#             marqueTelephone=dataset[['telephone']].iloc[i],
#             charismatique=dataset[['charismatique']].iloc[i],
#             gamer=dataset[['gamer']].iloc[i],
#             taille=dataset[['taille']].iloc[i],
#             projetPro=dataset[['projet_pro']].iloc[i],
#             stage=dataset[['stage']].iloc[i],
#             anneeNaissance=dataset[['annee_naissance']].iloc[i],
#             navigateur=dataset[['navigateur']].iloc[i],
#             os=dataset[['os']].iloc[i],
#             holeio=dataset[['hole_io']].iloc[i],
#             covid=dataset[['covid']].iloc[i],
#             dylan=dataset[['dylan']].iloc[i],
#             longueurCheveux=dataset[['longueur_cheveux']].iloc[i],
#             moisNaissance=dataset[['mois_naissance']].iloc[i],
#             fraternite=dataset[['fraternite']].iloc[i],
#             couleurYeux=dataset[['couleur_yeux']].iloc[i],
#             couleurCheveux=dataset[['couleur_cheveux']].iloc[i],
#             permis=dataset[['permis']].iloc[i]
#         )

#         struct.Ajouter(personne)

    
#     ptr = struct.tete

#     # remplir les voisins dans chaque maillon (liste des personnes incompatibles)
#     while ptr.suivant != None:
#         ptr2 = struct.tete
#         while ptr2.suivant != None:
#             if ptr.p.Comparer(ptr2.p) == False:
#                 ptr.voisins.append(ptr2.p)
#             ptr2 = ptr2.suivant
#         ptr = ptr.suivant
        
#     ptr = struct.tete

#     # remplir le graphe d'interaction avec les voisins 
#     while ptr.suivant != None:
#         # pour chaque ligne de la matrice
#         for voisin in ptr.voisins:
#             grapheInteraction[ptr.p.id][voisin.id] = 1
#         ptr = ptr.suivant

    
    # colorer le graphe d'interaction

if __name__ == "__main__":
    main()