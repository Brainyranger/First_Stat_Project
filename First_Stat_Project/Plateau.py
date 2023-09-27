import numpy as np

class Plateau:
    """
    Classe représentant un plateau de jeu rectangulaire.

    Attributes:
        nb_ligne (int): Le nombre de lignes du plateau.
        nb_colonne (int): Le nombre de colonnes du plateau.
        tableau (numpy.ndarray): Un tableau bidimensionnel (matrice) représentant le plateau de jeu, initialisé avec des zéros.

    """
    def __init__(self, nb_ligne, nb_colonne):
        """
        Initialise un plateau de jeu avec un nombre donné de lignes et de colonnes.

        Args:
            nb_ligne (int): Le nombre de lignes du plateau.
            nb_colonne (int): Le nombre de colonnes du plateau.
        """

        self.nb_ligne = nb_ligne
        self.nb_colonne = nb_colonne
        self.tableau = np.zeros((self.nb_ligne, self.nb_colonne), dtype=int)
    

   