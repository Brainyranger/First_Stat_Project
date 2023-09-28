import numpy as np

class Node:
    """
        Cette classe représente un noeud d'un arbre UCT 

        Args:
            jeu (objet de Jeu): L'objet de jeu sur lequel le joueur effectue son coup.
            joueur (objet de Joueur): L'objet de joueur qui va jouer le prochain coup.
            parent (objet de Jeu): Le noeud parent
            action (int): l'indice de la colonne jouée par ce noeud
        
        Attributs:
            racine (boolean): définie si le noeud est la racine de l'arbre
            joueur (objet de Joueur): L'objet de joueur qui va jouer le prochain coup.
            jeu (objet de Jeu): L'objet de jeu sur lequel le joueur effectue son coup.
            nb_visite (int): Le nombre de fois ou ce noeud a été visité
            nb_gagne (int):Le nombre de victoires
            enfants (List[Node]): La liste des noeuds enfants
            parent (objet de Jeu): Le noeud parent
            action (int): l'indice de la colonne jouée par ce noeud
    """
    def __init__(self, jeu, joueur, parent=None, action=None):
        self.racine = False
        self.joueur = joueur
        self.jeu = jeu
        self.nb_visite = 0
        self.nb_gagne = 0
        self.enfants = []
        self.parent = parent
        self.action = action

    

