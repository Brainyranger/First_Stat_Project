from Jeu import Jeu
from Plateau import Plateau
from Joueur import Joueur
from BanditManchot import BanditManchot
from Data import *
from Constante import *


def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Aléatoire")
        print("2. Bandit Manchot")
        print("3. Monte Carlo")
        print("4. UCT")
        print("5. Exit")

        choice = input("Votre choix: ")

        if choice == '1':
            data_run("data_experimental Joueur 1 vs Joueur 2", j1, j2, p, 50)
            break
        elif choice == '2':
            menu_bandit_manchot()
            break
        elif choice == '3':
            menu_Monte_Carlo()
            break
        elif choice == '4':
            menu_UCT()
            break
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Choix invalide")

def menu_Monte_Carlo():
    print("1. Monte Carlo vs Aléatoire")
    print("2. Monte Carlo vs Monte Carlo")

    choice = input("Votre choix: ")

    if choice == '1':
        data_MonteCarlovsAleatoire("data_experimental Joueur 1 vs Joueur 2", j1, j2, p, 50)
    elif choice == '2':
        data_MonteCarlo("data_experimental Joueur 1 vs Joueur 2", j1, j2, p, 50)
    else:
        print("Choix invalide")

def menu_bandit_manchot():
    print("1. Baseline Aleatoire")
    print("2. Greedy")
    print("3. eGreedy")
    print("4. UCB")

    choice = input("Votre choix: ")

    if choice == '1':
        data_baseline_aleatoire(100, jeu)
    elif choice == '2':
        data_greedyAlgorithmn(100, jeu)
    elif choice == '3':
        data_egreedy(100, 0.3, jeu)
    elif choice == '4':
        data_ucb(100,jeu)
    else:
        print("Choix invalide")

def menu_UCT():
    print("1. UCT vs Aléatoire")
    print("2. UCT vs Monte Carlo")

    choice = input("Votre choix: ")

    if choice == '1':
        data_UCTvsAleatoire("data_experimental Joueur 1 vs Joueur 2", j1, j2, p, 50)
    elif choice == '2':
        data_UCTvsMonteCarlo("data_experimental Joueur 1 vs Joueur 2", j1, j2, p, 50)
    else:
        print("Choix invalide")





p = Plateau(TAILLE_LIGNE, TAILLE_COLONNE)
j1 = Joueur(1, NB_JETON)
j2 = Joueur(-1, NB_JETON)
jeu = Jeu(p, j1, j2)

# data_UCTvsUCB("data_experimental Joueur 1 vs Joueur 2", j1, j2, p, 200)
# data_UCBvsGreedy("data_experimental Joueur 1 vs Joueur 2", j1, j2, p, 200)
# data_UCBvsEGreedy("data_experimental Joueur 1 vs Joueur 2", j1, j2, p, 200)
data_GreedyvsEGreedy("data_experimental Joueur 1 vs Joueur 2", j1, j2, p, 200)

# main_menu()


