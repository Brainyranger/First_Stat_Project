import numpy as np 
import random


class Jeu:

    def __init__(self, plateau,j1, j2):
        """ Initialisation d'un jeu de plateau avec les joueurs """
        self.j1 = j1
        self.j2 = j2
        self.plateau = plateau


    def play(self,x,joueur):
        """  Permet de placer un jeton dans la colonne x  pour le joueur spécifié """
        
        if joueur == self.j1:
            self.j1.compteur = self.j1.compteur - 1
            self.plateau[0][x] = 99

        if joueur == self.j2:
            self.j2.compteur = self.j2.compteur - 1
            self.plateau[0][x] = 99

    def is_finished(self):
        """ Permet de tester si c’est la fin du jeu (plateau plein ou victoire d’un joueur) """
        
        for line in self.plateau:
            for case in line:
                if case == 0:
                    print("Le plateau n'est pas plein")
                    break
                else:
                    continue 
            break
        
        if has_won() != 0:
            print("Victoire d'un joueur")
        else:
            print("plateau plein")
            
    def run(self,joueur1,joueur2):
        """permet de jouer une partie entre le joueur 1 et le joueur 2 : ils jouent à tour de rôle tant que la partie n’est pas finie.
            Elle renvoie 1 ou -1 selon la victoire du joueur 1 ou 2, et 0 en cas de nul."""

            codage_joueur = [1,-1]
            premier_joueur = codage_joueur[random.randint(0,1)] 
            if premier_joueur == self.j1:
                deuxième_joueur = self.j2
            else: 
                premier_joueur = self.j2
                deuxième_joueur = self.j1
            
             while True:

                premier_joueur.play(self.plateau,premier_joueur)
                deuxieme_joueur.play(self.plateau,deuxieme_joueur)
                
                if has_won()==premier_joueur:
                    return premier_joueur
                elif has_won()==deuxieme_joueur:
                    return deuxieme_joueur
                else:
                    return 0
