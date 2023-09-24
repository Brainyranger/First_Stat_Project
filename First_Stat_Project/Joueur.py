import numpy as np
from Constante import NB_PARTI

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
        actions = np.array(jeu.colonne_disponible())  # Convertir en un tableau NumPy
        actions = np.column_stack((actions, np.zeros(actions.shape[0], dtype=int)))  # Ajouter la colonne de récompenses

        for i in range(1, NB_PARTI):
            action = np.random.choice(actions[:, 0])  # Choisir une action au hasard

            copie_jeu = jeu.copie()

            gagnant = copie_jeu.run()

            if gagnant == self.id_joueur:
                # Trouver l'index de l'action sélectionnée dans le tableau
                index = np.where(actions[:, 0] == action)[0][0]
                actions[index, 1] += 1
                
        max_index = np.argmax(actions[:, 1])
        max_action = actions[max_index, 0]

        return max_action
        

