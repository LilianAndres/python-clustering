from itertools import count

from numpy import char


class Personne:
    
    _id = count(0)

    def __init__(self, nom, tempsTrajet, marqueTelephone, charismatique, gamer, taille, projetPro, stage, anneeNaissance, navigateur, os, holeio, covid, dylan, longueurCheveux, moisNaissance, fraternite, couleurYeux, couleurCheveux, permis):
        # identification
        self.id = next(self._id)
        self.nom = nom
        # métriques principales
        self.tempsTrajet = tempsTrajet
        self.marqueTelephone = marqueTelephone
        self.charismatique = charismatique
        self.gamer = gamer
        self.taille = taille 
        self.projetPro = projetPro
        self.stage = stage
        self.anneeNaissance = anneeNaissance
        self.navigateur = navigateur
        self.os = os
        # sous-métriques
        self.holeio = holeio
        self.covid = covid
        self.dylan = dylan
        self.longueurCheveux = longueurCheveux
        self.moisNaissance = moisNaissance
        self.fraternite = fraternite
        self.couleurYeux = couleurYeux
        self.couleurCheveux = couleurCheveux
        self.permis = permis
        


    def Comparer(self, personne):
        """Compare deux personnes en fonction de leurs métriques et de leurs sous-métriques"""

        compatibilite = 0

        if self.marqueTel == personne.marqueTel:
            compatibilite += 3
        if self.jeux == personne.jeux:
            compatibilite += 4
        if self.isContamined == personne.isContamined:
            compatibilite += 1
        if self.taille == personne.taille:
            compatibilite += 2
        if self.projetPro == personne.projetPro:
            compatibilite += 3
        if self.possedeStage == personne.possedeStage:
            compatibilite += 1
        if self.moisNaissance == personne.moisNaissance:
            compatibilite += 1
        if self.possedePermis == personne.possedePermis:
            compatibilite += 2

        if compatibilite > 5:
            return True
        return False
        

