from Maillon import Maillon


class Struct:

    def __init__(self):
        self.tete = None

    
    def Ajouter(self, personne):
        if self.tete == None:
            self.tete = Maillon(personne, None, None)
        else:
            temp = self.tete
            while temp.suivant != None:
                temp = temp.suivant
            temp.suivant = Maillon(personne, temp, None)


    def Afficher(self):
        ptr = self.tete
        while ptr != None:
            print("Nom: " + str(ptr.p.id))
            if ptr.precedent != None:
                print("Précédent: " + str(ptr.precedent.p.id))
            else:
                print("Précédent: NONE")
            if ptr.suivant != None:
                print("Suivant: " + str(ptr.suivant.p.id))
            else:
                print("Suivant: NONE")
            print("Voisins: ")
            for i in range(len(ptr.voisins)):
                print(ptr.voisins[i].id)
            print("----------------------------------------")
            ptr = ptr.suivant
