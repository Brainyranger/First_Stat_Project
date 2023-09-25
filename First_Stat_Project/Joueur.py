import numpy as np
from Constante import NB_PARTI

class Joueur:
       """
    Classe représentant un joueur pour un jeu de plateau.

    Attributes:
        id_joueur (int): L'identifiant du joueur.
        nb_jetons (int): Le nombre de jetons disponibles pour le joueur.
        nb_parti_gagner (int): Le nombre de parties gagnées par le joueur.
        nb_parti_perdu (int): Le nombre de parties perdues par le joueur.
        nb_parti_egalite (int): Le nombre de parties terminées en égalité par le joueur.

    Methods:
        play(jeu): Méthode pour effectuer un coup aléatoire.
        play_MonteCarlo(jeu): Méthode pour effectuer un coup en utilisant la méthode Monte Carlo.
    """
    def __init__(self, id_joueur, nb_jetons):
        """
        Initialise un joueur avec un identifiant et un nombre de jetons.

        Args:
            id_joueur (int): L'identifiant du joueur.
            nb_jetons (int): Le nombre de jetons disponibles pour le joueur.
        """
        self.id_joueur = id_joueur
        self.nb_jetons = nb_jetons
        self.nb_parti_gagner = 0
        self.nb_parti_perdu = 0
        self.nb_parti_egalite = 0

       

    def play(self, jeu):
        """
        Effectue un coup aléatoire en choisissant une colonne disponible au hasard.

        Args:
            jeu (objet de jeu): L'objet de jeu sur lequel le joueur effectue son coup.

        Returns:
            int: L'indice de la colonne choisie.
        """

        if self.nb_jetons>0:
            colonne_disponible = jeu.colonne_disponible()#liste de colonne disponible présent dans le plateau 
            if len(colonne_disponible)!=0:
                return np.random.choice(jeu.colonne_disponible(),1)[0]#choix de la colonne où l'on insère le jeton
            else:
                print("Il ne reste plus de colonne disponible")
        else:
            print("Il reste 0 jeton")



    def play_MonteCarlo(self, jeu):
        """
        Effectue un coup en utilisant la méthode Monte Carlo pour choisir la meilleure action.

        Args:
            jeu (objet de jeu): L'objet de jeu sur lequel le joueur effectue son coup.

        Returns:
            int: L'indice de la colonne choisie en utilisant la méthode Monte Carlo.
        """


        actions = np.array(jeu.colonne_disponible())  # Convertir en un tableau NumPy
        actions = np.column_stack((actions, np.zeros(actions.shape[0], dtype=int)))  # Ajouter la colonne de récompenses

        # Simulez plusieurs parties (NB_PARTI) pour évaluer les actions
        for i in range(1, NB_PARTI):
            action = np.random.choice(actions[:, 0])  # Choisir une action au hasard

            copie_jeu = jeu.copie() # Copiez le jeu pour simuler le coup sans affecter le jeu original

            gagnant = copie_jeu.run()

            if gagnant == self.id_joueur: # Si le joueur actuel (celui qui utilise Monte Carlo) a gagné, mettez à jour la récompense de l'action

                # Trouver l'index de l'action sélectionnée dans le tableau
                index = np.where(actions[:, 0] == action)[0][0]
                actions[index, 1] += 1

        # Sélectionnez l'action avec le plus grand nombre de récompenses accumulées        
        max_index = np.argmax(actions[:, 1])
        max_action = actions[max_index, 0]

        return max_action
        

