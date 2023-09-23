import numpy as np
import matplotlib.pyplot as plt
from Jeu import Jeu
from Plateau import Plateau
from Constante import NB_JETON
from Joueur import Joueur
from BanditManchot import BanditManchot
from scipy.stats import kde
from Data import data_run,data_baseline_aleatoire,data_greedyAlgorithmn,data_egreedy,data_ucb

#création du jeu

p = Plateau(100,170)
j1 = Joueur(1,21)
j2 = Joueur(-1,21)
jeu = Jeu(p,j1,j2)

#data_run("data_experimental Joueur 1 vs Joueur 2",j1,j2,p,50)

#Bandit Manchot 

machine_sous = BanditManchot()

#print(machine_sous.baseline_aleatoire())
#print(machine_sous.greedy_algorithm())
#print(machine_sous.e_greedy(0.3))
#print(machine_sous.ucb())

#data_baseline_aleatoire(100)
#data_greedyAlgorithmn(100)
#data_egreedy(100,0.3)
data_ucb(100)