import numpy as np
from Constante import NB_PARTI
import random

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

    def play_MonteCarlo(self, jeu):
        actions = jeu.colonne_disponible()
        actions = [[action,0] for action in actions]

        for i in range(1,NB_PARTI):
            action = random.choice(actions)[0]
            # copie_jeu = Jeu(jeu.plateau,jeu.j1,jeu.j2)
            copie_jeu = jeu.copie()

            gagnant = copie_jeu.run()

            if(gagnant == self.id_joueur):
                for j in range(0,len(actions)):
                    if actions[j][0]==action:
                        actions[j][1]+=1

        max_action = actions[0]
        for i in range(1, len(actions)):
            if (actions[i][1] > max_action[1]):
                max_action = actions[i]
        
        return max_action[0]







