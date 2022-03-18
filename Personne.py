from itertools import count


class Personne:
    
    _id = count(0)

    def __init__(self, nom, marqueTel, jeux, isContamined, taille, projetPro, possedeStage, moisNaissance, possedePermis):
        self.id = next(self._id)
        self.nom = nom
        self.marqueTel = marqueTel
        self.jeux = jeux
        self.isContamined = isContamined
        self.taille = taille
        self.projetPro = projetPro
        self.possedeStage = possedeStage
        self.moisNaissance = moisNaissance
        self.possedePermis = possedePermis


    def Comparer(self, personne):
        """Compare deux personnes en fonction de leurs métriques"""

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
        

