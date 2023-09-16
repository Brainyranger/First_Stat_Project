import numpy as np
import matplotlib.pyplot as plt
from Jeu import Jeu
from Plateau import Plateau
from Constante import NB_JETON
from Joueur import Joueur
from scipy.stats import kde
from Data import data_run

#création du jeu

p = Plateau(100,170)
j1 = Joueur(1,21)
j2 = Joueur(-1,21)
data_run("data_experimental Joueur 1 vs Joueur 2",j1,j2,p,50)

