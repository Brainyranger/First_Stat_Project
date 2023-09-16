import numpy as np

class Joueur:
    def __init__(self, id_joueur, nb_jetons):
        self.id_joueur = id_joueur
        self.nb_jetons = nb_jetons
        self.nb_parti_gagner = 0
        self.nb_parti_perdu = 0
        self.nb_parti_egalite = 0

       

    def play(self, jeu):
        if self.nb_jetons>0:
            return np.random.choice(jeu.colonne_disponible(),1)[0]
        else:
            print("Il reste 0 jeton")




        

