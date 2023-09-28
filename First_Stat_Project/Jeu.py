import numpy as np 
from Plateau import Plateau
from UCT import UCT
from Constante import *



class Jeu:
    """
    Classe représentant un jeu de plateau où deux joueurs s'affrontent.

    Attributes:
        plateau (Plateau): L'objet Plateau représentant le plateau de jeu.
        j1 (Joueur): Le premier joueur.
        j2 (Joueur): Le deuxième joueur.
        nb_jeton_jouer (int): Le nombre total de jetons joués dans la partie.
        gagnant (int): L'identifiant du joueur gagnant (1 ou 2) ou 0 en cas de nul.

    Methods:
        reset(): Réinitialise le jeu pour une nouvelle partie.
        colonne_disponible(): Renvoie la liste des indices des colonnes disponibles pour jouer.
        play(x, joueur): Permet à un joueur de placer un jeton dans une colonne spécifiée.
        positions_gagnantes(): Liste de toutes les positions gagnantes possibles sur le plateau.
        has_won(): Vérifie si l'un des joueurs a gagné en parcourant les positions gagnantes.
        is_finished(): Vérifie si la partie est terminée, que ce soit par une victoire d'un joueur ou un plateau plein (égalité).
        run(): Permet de jouer une partie entre les deux joueurs en alternant leurs tours jusqu'à ce que la partie se termine.
        run_monte_carlo_vs_aleatoire(): Permet de jouer une partie où le joueur 1 utilise la méthode Monte Carlo pour choisir ses coups, tandis que le joueur 2 joue de manière aléatoire.
        run_monte_carlo(): Permet de jouer une partie où les deux joueurs utilisent la méthode Monte Carlo pour choisir leurs coups.
        copie(): Crée une copie du jeu actuel.
    """

    def __init__(self, plateau,j1, j2):
        """
        Initialisation d'un jeu de plateau avec les joueurs.

        Args:
            plateau (Plateau): L'objet Plateau représentant le plateau de jeu.
            j1 (Joueur): Le premier joueur.
            j2 (Joueur): Le deuxième joueur.
        """
        self.j1 = j1
        self.j2 = j2
        self.nb_jeton_jouer = 0
        self.plateau = plateau
        self.gagnant = 0
        self.reset()
       
     



    def reset(self):
        """
        Réinitialise le jeu pour une nouvelle partie en remettant à zéro le plateau, les jetons des joueurs,
        et le nombre de jetons joués.
        """
        self.plateau = Plateau(TAILLE_LIGNE,TAILLE_COLONNE)
        self.nb_jeton_jouer = 0
        self.j1.nb_jetons = NB_JETON
        self.j2.nb_jetons = NB_JETON
      
       


    def colonne_disponible(self):
        """
        Renvoie la liste des indices des colonnes disponibles pour jouer.
        """
        col = []
        for i in range(self.plateau.nb_colonne):
            if self.plateau.tableau[0][i] == 0:# On vérifie que l'indice d'une colonne soit disponible
                col.append(i)
        return col

    def play(self,x,joueur):
        """
        Permet à un joueur de placer un jeton dans la colonne spécifiée.

        Args:
            x (int): L'indice de la colonne dans laquelle le coup est joué.
            joueur (Joueur): Le joueur qui joue le coup.
        """
        

        max_index = (self.plateau.tableau[:, x] != 0).argmax() 
        if 0 <= max_index < self.plateau.nb_ligne:
            self.plateau.tableau[(self.plateau.tableau[:,x] != 0).argmax()-1, x] = joueur.id_joueur
            self.nb_jeton_jouer += 1
            joueur.nb_jetons -=1
        else:
            print("Indice de ligne invalide. Réessayez avec une colonne valide.")
        

    def positions_gagnantes(self):
        """
        Liste de toutes les positions gagnantes possibles sur le plateau.

        Returns:
            numpy.array: Un tableau NumPy contenant les positions gagnantes.
        """

        return np.array([
        [ [j, j + dj, j + 2*dj, j + 3*dj], [i, i + di, i + 2*di, i + 3*di] ]for j in range(0,self.plateau.nb_ligne) for i in range(0,self.plateau.nb_colonne) for di, dj in [(-1,1), (1,0), (0,1), (1,1)]
        if (0 <= i + 3 * di < self.plateau.nb_colonne and 0 <= j + 3 * dj < self.plateau.nb_ligne)
        ])



    def has_won(self):
        """
        Vérifie si l'un des joueurs a gagné en parcourant les positions gagnantes.

        Returns:
            bool: True si l'un des joueurs a gagné, False sinon.
        """

        liste_gagnante = self.positions_gagnantes()
        for i in range(len(liste_gagnante)):
            if np.all(self.plateau.tableau[tuple(liste_gagnante[i])] == self.j1.id_joueur):#vérifie si le joueur 1 à gagner
                self.gagnant = self.j1.id_joueur
                return True
            if np.all(self.plateau.tableau[tuple(liste_gagnante[i])] == self.j2.id_joueur):#vérifie si le joueur 2 à gagner
                self.gagnant = self.j2.id_joueur
                return True
        return False 

    def is_finished(self):
        """
        Vérifie si la partie est terminée, que ce soit par une victoire d'un joueur ou un plateau plein (égalité).

        Returns:
            bool: True si la partie est terminée, False sinon.
        """
        
        
        if self.has_won():
            print("Victoire d'un joueur"+" ayant pour ID "+str(self.gagnant))

            # update des caractéristiques du joueur 1
            if self.gagnant == self.j1.id_joueur:
                self.j1.nb_parti_gagner += 1 
                self.j2.nb_parti_perdu  += 1
            else:
                # update des caractéristiques du joueur 1
                self.j2.nb_parti_gagner += 1 
                self.j1.nb_parti_perdu  += 1
            return True

        elif self.nb_jeton_jouer == self.plateau.nb_ligne*self.plateau.nb_colonne: #cas d'égalité 
            self.j1.nb_parti_egalite += 1 
            self.j2.nb_parti_egalite += 1

            print("plateau plein")
            return True

        else:

            return False

            
    def run(self):
        """
        Permet de jouer une partie entre les deux joueurs en alternant leurs tours jusqu'à ce que la partie se termine.

        Returns:
            int: L'identifiant du joueur gagnant (1 ou 2) ou 0 en cas de nul.
        """

        while not self.is_finished():
            self.play(self.j1.play(self),self.j1)#joueur 1 joue de manière aléatoire
            self.play(self.j2.play(self),self.j2)#joueur 2 joue de manière aléatoire

        if self.nb_jeton_jouer == self.plateau.nb_ligne*self.plateau.nb_colonne: #si le jeu se termine, on vérifie si il y a eu égalité
            return 0
        
        return self.gagnant


    def run_monte_carlo_vs_aleatoire(self):
        """
        Permet de jouer une partie où le joueur 1 utilise la méthode Monte Carlo pour choisir ses coups,
        tandis que le joueur 2 joue de manière aléatoire.

        Returns:
            int: L'identifiant du joueur gagnant (1 ou 2) ou 0 en cas de nul.
        """

        while not self.is_finished():
            self.play(self.j1.play_MonteCarlo(self), self.j1)#joueur 1 joue avec la stratégie MonteCarlo
            self.play(self.j2.play(self),self.j2)#joueur 2 joue de manière aléatoire 
        

        if self.nb_jeton_jouer == self.plateau.nb_ligne*self.plateau.nb_colonne: # Test du match nul 
            return 0
        
        return self.gagnant

    def run_monte_carlo(self):
        """
        Permet de jouer une partie où les deux joueurs utilisent la méthode Monte Carlo pour choisir leurs coups.

        Returns:
            int: L'identifiant du joueur gagnant (1 ou 2) ou 0 en cas de nul.
        """

        while not self.is_finished():
            self.play(self.j1.play_MonteCarlo(self), self.j1)#joueur 1 joue avec la stratégie MonteCarlo
            self.play(self.j2.play_MonteCarlo(self),self.j2)#joueur 2 joue avec la stratégie MonteCarlo
           

        if self.nb_jeton_jouer == self.plateau.nb_ligne*self.plateau.nb_colonne: # Test du match nul 
            return 0
        
        return self.gagnant
    
    def run_uct_vs_alea(self):
        """
        Permet de jouer une partie où le joueur 1 utilise la méthode UCT pour choisir ses coups,
        tandis que le joueur 2 joue de manière aléatoire.

        Returns:
            int: L'identifiant du joueur gagnant (1 ou 2) ou 0 en cas de nul.
        """
        while not self.is_finished():
            uct = UCT(self, self.j1)
            self.play(uct.play_uct(NB_PARTI), self.j1)#joueur 1 joue avec la stratégie MonteCarlo
            self.play(self.j2.play(self),self.j2)#joueur 2 joue avec la stratégie MonteCarlo
           

        if self.nb_jeton_jouer == self.plateau.nb_ligne*self.plateau.nb_colonne: # Test du match nul 
            return 0
        
        return self.gagnant
    
    def run_uct_vs_monte_carlo(self):
        """
        Permet de jouer une partie où le joueur 1 utilise la méthode UCT pour choisir ses coups,
        tandis que le joueur 2 utilise la méthode monte carlo.

        Returns:
            int: L'identifiant du joueur gagnant (1 ou 2) ou 0 en cas de nul.
        """
        while not self.is_finished():
            uct = UCT(self, self.j1)
            self.play(uct.play_uct(NB_PARTI), self.j1)#joueur 1 joue avec la stratégie MonteCarlo
            self.play(self.j2.play_MonteCarlo(self),self.j2)#joueur 2 joue avec la stratégie MonteCarlo
           

        if self.nb_jeton_jouer == self.plateau.nb_ligne*self.plateau.nb_colonne: # Test du match nul 
            return 0
        
        return self.gagnant

    
    def copie(self):
        """
        Crée une copie du jeu actuel en instanciant un nouvel objet Jeu avec les mêmes attributs plateau, j1 et j2.

        Returns:

        Jeu: Un nouvel objet Jeu qui est une copie du jeu actuel.

        """
        return Jeu(self.plateau, self.j1, self.j2)
        


