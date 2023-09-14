import numpy as np 
import random
from Joueur import Joueur
from Plateau import Plateau

TAILLE_COLONNE = 7
TAILLE_LIGNE  = 6

class Jeu:


    def __init__(self, plateau,j1, j2):
        """ Initialisation d'un jeu de plateau avec les joueurs """
        self.j1 = j1
        self.j2 = j2
        self.j_courant = j1 #par défault
        self.nb_jeton_jouer = 0
        self.plateau = plateau
        self.gagnant = 0
        self.reset()
       
     



    def reset(self):
        """ réinitialise du jeu """
        self.plateau = Plateau(TAILLE_LIGNE,TAILLE_COLONNE)
        self.nb_jeton_jouer = 0
        self.j_courant = self.j1
        self.j1.reset_joueur()
        self.j2.reset_joueur()
      
       

    def change_jcourant(self):
        """change le joueur courant"""

        if self.j_courant.id_joueur == self.j1.id_joueur:
            self.j_courant.nb_jetons -=1
            self.j_courant = self.j2

        else:
            self.j_courant.nb_jetons -=1
            self.j_courant = self.j1

    def colonne_disponible(self):
        """Retourne toutes les colonnes où on peut placer un jeton"""
        col = []
        for i in range(self.plateau.nb_colonne):
            if self.plateau.tableau[0][i] == 0:
                col.append(i)
        return col

    def play(self,x,joueur):
        """  Permet de placer un jeton dans la colonne x pour le joueur spécifié """
        

        max_index = (self.plateau.tableau[:, x] != 0).argmax() 
        if 0 <= max_index < self.plateau.nb_ligne:
            self.plateau.tableau[(self.plateau.tableau[:,x] != 0).argmax()-1, x] = joueur.id_joueur
            self.nb_jeton_jouer += 1
        else:
            print("Indice de ligne invalide. Réessayez avec une colonne valide.")
        

    def positions_gagnantes(self):
        """ liste de toutes les positions gagnantes """

        return np.array([
        [ [j, j + dj, j + 2*dj, j + 3*dj], [i, i + di, i + 2*di, i + 3*di] ]for j in range(0,self.plateau.nb_ligne) for i in range(0,self.plateau.nb_colonne) for di, dj in [(-1,1), (1,0), (0,1), (1,1)]
        if (0 <= i + 3 * di < self.plateau.nb_colonne and 0 <= j + 3 * dj < self.plateau.nb_ligne)
        ])

    def has_won(self):
        """ une fonction has_won() qui permet de tester la victoire d’un des deux joueurs """

        liste_gagnante = self.positions_gagnantes()
        for i in range(len(liste_gagnante)):
            if np.all(self.plateau.tableau[tuple(liste_gagnante[i])] == self.j1.id_joueur):
                self.gagnant = self.j1.id_joueur
                return True
            if np.all(self.plateau.tableau[tuple(liste_gagnante[i])] == self.j2.id_joueur):
                self.gagnant = self.j2.id_joueur
                return True
        return False

    def is_finished(self):
        """ Permet de tester si c’est la fin du jeu (plateau plein ou victoire d’un joueur) """
        
        
        if self.has_won():
            print("Victoire d'un joueur"+" ayant pour ID "+str(self.gagnant))
            if self.gagnant == self.j1.id_joueur:
                self.j1.nb_parti_gagner += 1 
                self.j2.nb_parti_perdu  += 1
            else:
                self.j2.nb_parti_gagner += 1 
                self.j1.nb_parti_perdu  += 1
            return True

        elif self.nb_jeton_jouer == self.plateau.nb_ligne*self.plateau.nb_colonne:
            self.j1.nb_parti_egalite += 1 
            self.j2.nb_parti_egalite += 1

            print("plateau plein")
            return True
        else:
            print("plateau pas plein")
            return False

            
    def run(self):
        """permet de jouer une partie entre le joueur 1 et le joueur 2 : ils jouent à tour de rôle tant que la partie n’est pas finie.
            Elle renvoie 1 ou -1 selon la victoire du joueur 1 ou 2, et 0 en cas de nul."""

        while not self.is_finished():
            self.play(self.j_courant.play(self),self.j_courant)
            self.change_jcourant()
            print("Il reste au joueur "+str(self.j1.id_joueur)+" "+str(self.j1.nb_jetons)+" jetons")
            print("Il reste au joueur "+str(self.j2.id_joueur)+" "+str(self.j2.nb_jetons)+" jetons")
            print("\n")

        if self.nb_jeton_jouer == self.plateau.nb_ligne*self.plateau.nb_colonne:
            return 0
        
        return self.gagnant

        


p = Plateau(6,7)
j1 = Joueur(1,21)
j2 = Joueur(-1,21)

jeu = Jeu(p,j1,j2)
#print(jeu.positions_gagnantes())

jeu.run()
#jeu.reset()