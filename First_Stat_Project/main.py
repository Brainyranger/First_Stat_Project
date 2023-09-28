from Jeu import Jeu
from Plateau import Plateau
from Joueur import Joueur
from BanditManchot import BanditManchot
from UCT import UCT
from Data import *
#création du jeu

p = Plateau(100,170)
j1 = Joueur(1,21)
j2 = Joueur(-1,21)
jeu = Jeu(p,j1,j2)

#puissance 4 

#data_run("data_experimental Joueur 1 vs Joueur 2",j1,j2,p,50)

#MonteCarlo

# data_MonteCarlovsAleatoire("data_experimental Joueur 1 vs Joueur 2",j1,j2,p,50)
# data_MonteCarlo("data_experimental Joueur 1 vs Joueur 2",j1,j2,p,50)


#Bandit Manchot 

machine_sous = BanditManchot(jeu)

#print(machine_sous.baseline_aleatoire())
#print(machine_sous.greedy_algorithm())
#print(machine_sous.e_greedy(0.3))
#print(machine_sous.ucb())

#data_baseline_aleatoire(100,jeu)
#data_greedyAlgorithmn(100,jeu)
#data_egreedy(100,0.3,jeu)
# data_ucb(100,jeu)


# uct = UCT(jeu, j1)
# action = uct.play_uct(10)

data_UCTvsAleatoire("data_experimental Joueur 1 vs Joueur 2",j1,j2,p,50)

# data_UCTvsMonteCarlo("data_experimental Joueur 1 vs Joueur 2",j1,j2,p,50)
