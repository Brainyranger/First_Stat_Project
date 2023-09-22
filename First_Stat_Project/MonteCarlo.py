import random
from Jeu import Jeu
from Constante import NB_PARTI

class MonteCarlo:
    def __init__(self,jeu):
        #self.etat = f"Dans le plateau {jeu.plateau.nb_ligne}x{jeu.plateau.nb_colonne},le joueur {self.j1} commence."
        self.jeu = jeu

    def play_MonteCarlo(self,joueur):
        actions = self.jeu.colonne_disponible()
        actions = [[action,0] for action in actions]

        for i in range(1,NB_PARTI):
            action = random.choice(actions)[0]
            copie_jeu = Jeu(self.jeu.plateau,self.jeu.j1,self.jeu.j2)

            gagnant = copie_jeu.run()

            if(gagnant == joueur.id_joueur):
                for j in range(0,len(actions)):
                    if actions[j][0]==action:
                        actions[j][1]+=1
            
            print(actions)

        max_action = actions[0]
        for i in range(1, len(actions)):
            if (actions[i][1] > max_action[1]):
                max_action = actions[i]
        
        return max_action[0]