import numpy as np 


class Plateau:

    def __init__(self,nb_ligne,nb_colonne):
        """ Initialisation d'un plateau de nb_ligne * nb_colonne """

        self.ligne = nb_ligne
        self.colonne = nb_colonne
        self.plateau = []


    def reset_plateau(self):
        """ Réinitialise le plateau """

        i : int 
        j : int
        for i in range(0,self.ligne):
            for j in range(0,self.colonne):
                self.plateau [i][j] = 0

    
    def succes_plateau(self):
        """ Renvoie une liste des listes des positions répondant aux exigences du puissance 4 """