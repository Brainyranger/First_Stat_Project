import numpy as np

class Joueur:
    def __init__(self, id_joueur, nb_jetons):
        self.id_joueur = id_joueur
        self.nb_jetons = nb_jetons
        self.jetons = np.arange(0, nb_jetons) #[id_joueur for i in range(0, nb_jetons)]
        self.jeton_courant = 0

    def play(self, plateau, joueur):
        if joueur.jeton_courant < len(joueur.jetons):
            coups_possibles = []
            for i in range(0, plateau.nb_ligne):
                coups_possibles.append((plateau.tableau[i, :]==0).argmax())
                
                # j = 0
                # while j < plateau.nb_ligne:
                #     if plateau.tableau[j][i] == 0:
                #         coups_possibles = np.append(coups_possibles, (j, i)) #coups_possibles.append((j, i))
                #         break
                #     else:
                #         j += 1
            
            #return random.choice(coups_possibles)
            return np.random.choice(coups_possibles)
        
        else:
            print("Il vous reste 0 jetons")

            return 0




        

