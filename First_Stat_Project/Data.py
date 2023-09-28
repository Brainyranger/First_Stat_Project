import numpy as np
import matplotlib.pyplot as plt
from Jeu import Jeu
from Plateau import Plateau
from Constante import NB_JETON,NOMBRE_LEVIERS
from Joueur import Joueur
from BanditManchot import BanditManchot
from scipy.stats import kde




def data_run(title, joueur1, joueur2, plateau, nb_parts):
    """
    Lance une partie entre 2 joueurs et étudie le nombre de coups jusqu'à une victoire, pour le joueur 1 et pour le joueur 2.

    Args:
        title (str): Le titre de l'expérience.
        joueur1 (Joueur): Le joueur 1.
        joueur2 (Joueur): Le joueur 2.
        plateau (Plateau): L'objet Plateau représentant le plateau de jeu.
        nb_parts (int): Le nombre de parties à jouer.

    """


    jeu = Jeu(plateau,joueur1,joueur2)
    res_joueur1 = []
    res_joueur2 = []
    for i in range(0,nb_parts):
        gagnat = jeu.run() 
        if jeu.gagnant == joueur1.id_joueur:
            res_joueur1.append(NB_JETON-jeu.j1.nb_jetons)
        if jeu.gagnant == joueur2.id_joueur:
            res_joueur2.append(NB_JETON-jeu.j2.nb_jetons)
          

        jeu.reset()

    
   
    print(title)
    print("Nb parties nulles\t:", jeu.j1.nb_parti_egalite)
    print("Nb parties gagnées joueur 1\t:", jeu.j1.nb_parti_gagner)
    print("Nb parties gagnées joueur 2\t:", jeu.j2.nb_parti_gagner)


    #trace l'histogramme de la distribution du nb de victoire en fonction du nb de coup
    plt.figure(f"histogramme {title}")
    plt.hist(np.array(res_joueur1),bins=25,label="joueur 1")
    plt.hist(np.array(res_joueur2),bins=25,label="joueur 2")
    plt.ylabel("Nb victoires")
    plt.xlabel("Nb Coups")

    #trace le graphique de densite
    plt.figure(f"graphique {title}")
    density_1 = kde.gaussian_kde(np.array(res_joueur1))
    density_2 = kde.gaussian_kde(np.array(res_joueur2))
    x = np.linspace(4,20,300)
    y1 = density_1(x)
    y2 = density_2(x) 
    plt.plot(x,y1,label="joueur 1")
    plt.plot(x,y2,label="joueur 2")
    plt.ylabel("Densité")
    plt.xlabel("Nombre de Coups")
    
    
    plt.legend()
    plt.grid()
    plt.show()
   

def data_MonteCarlo(title, joueur1, joueur2, plateau, nb_parts):
    """
    Lance une partie entre 2 joueurs utilisant la méthode Monte Carlo pour choisir les coups,
    et étudie le nombre de coups jusqu'à une victoire, pour le joueur 1 et pour le joueur 2.

    Args:
        title (str): Le titre de l'expérience.
        joueur1 (Joueur): Le joueur 1.
        joueur2 (Joueur): Le joueur 2.
        plateau (Plateau): L'objet Plateau représentant le plateau de jeu.
        nb_parts (int): Le nombre de parties à jouer.
    """

    jeu = Jeu(plateau,joueur1,joueur2)
    res_joueur1 = []
    res_joueur2 = []
    for i in range(0,nb_parts):
        gagnat = jeu.run_monte_carlo() 
        if jeu.gagnant == joueur1.id_joueur:
            res_joueur1.append(NB_JETON-jeu.j1.nb_jetons)
        if jeu.gagnant == joueur2.id_joueur:
            res_joueur2.append(NB_JETON-jeu.j2.nb_jetons)
        jeu.reset()


    
    print(title)
    print("Nb parties nulles\t:", jeu.j1.nb_parti_egalite)
    print("Nb parties gagnées joueur 1\t:", jeu.j1.nb_parti_gagner)
    print("Nb parties gagnées joueur 2\t:", jeu.j2.nb_parti_gagner)

    #trace l'histogramme de la distribution du nb de victoire en fonction du nb de coup
    plt.figure(f"histogramme {title}")
    plt.hist(np.array(res_joueur1),bins=25,label="joueur 1")
    plt.hist(np.array(res_joueur2),bins=25,label="joueur 2")
    plt.ylabel("Nb victoires")
    plt.xlabel("Nb Coups")

    #trace le graphique de densite
    plt.figure(f"graphique {title}")
    density_1 = kde.gaussian_kde(np.array(res_joueur1))
    density_2 = kde.gaussian_kde(np.array(res_joueur2))
    x = np.linspace(4,20,300)
    y1 = density_1(x)
    y2 = density_2(x) 
    plt.plot(x,y1,label="joueur 1")
    plt.plot(x,y2,label="joueur 2")
    plt.ylabel("Densité")
    plt.xlabel("Nombre de Coups")
    
    
    plt.legend()
    plt.grid()
    plt.show()

def data_MonteCarlovsAleatoire(title, joueur1, joueur2, plateau, nb_parts):
    """
    Lance une partie entre 2 joueurs, où le joueur 1 utilise la méthode Monte Carlo pour choisir les coups,
    et le joueur 2 joue de manière aléatoire, et étudie le nombre de coups jusqu'à une victoire, pour le joueur 1 et pour le joueur 2.

    Args:
        title (str): Le titre de l'expérience.
        joueur1 (Joueur): Le joueur 1 (utilisant Monte Carlo).
        joueur2 (Joueur): Le joueur 2 (jouant de manière aléatoire).
        plateau (Plateau): L'objet Plateau représentant le plateau de jeu.
        nb_parts (int): Le nombre de parties à jouer.
    """

    jeu = Jeu(plateau,joueur1,joueur2)
    res_joueur1 = []
    res_joueur2 = []
    for i in range(0,nb_parts):
        gagnat = jeu.run_monte_carlo_vs_aleatoire() 
        if jeu.gagnant == joueur1.id_joueur:
            res_joueur1.append(NB_JETON-jeu.j1.nb_jetons)
        if jeu.gagnant == joueur2.id_joueur:
            res_joueur2.append(NB_JETON-jeu.j2.nb_jetons)
        jeu.reset()


    
    print(title)
    print("Nb parties nulles\t:", jeu.j1.nb_parti_egalite)
    print("Nb parties gagnées joueur 1\t:", jeu.j1.nb_parti_gagner)
    print("Nb parties gagnées joueur 2\t:", jeu.j2.nb_parti_gagner)
    
    #trace l'histogramme de la distribution du nb de victoire en fonction du nb de coup
    plt.figure(f"histogramme {title}")
    plt.hist(np.array(res_joueur1),bins=25,label="joueur 1")
    plt.hist(np.array(res_joueur2),bins=25,label="joueur 2")
    plt.ylabel("Nb victoires")
    plt.xlabel("Nb Coups")

     #trace le graphique de densite
    plt.figure(f"graphique {title}")
    density_1 = kde.gaussian_kde(np.array(res_joueur1))
    density_2 = kde.gaussian_kde(np.array(res_joueur2))
    x = np.linspace(4,20,300)
    y1 = density_1(x)
    y2 = density_2(x) 
    plt.plot(x,y1,label="joueur 1")
    plt.plot(x,y2,label="joueur 2")
    plt.ylabel("Densité")
    plt.xlabel("Nombre de Coups")
    
    
    plt.legend()
    plt.grid()
    plt.show()

def data_baseline_aleatoire(nombre_iteration,jeu):
    """
    Effectue des simulations avec un bandit manchot utilisant la stratégie "baseline aléatoire".

    Args:
        nombre_iteration (int): Le nombre d'itérations pour les simulations.
    """

    bandit_aleatoire = BanditManchot(jeu)
    rec_moy_est =  [0.0] * len(jeu.colonne_disponible())
    nb_fois =  [0]* len(jeu.colonne_disponible())
    temps = np.arange(nombre_iteration)
    regret_cumule = np.zeros(nombre_iteration)

    for i in range(nombre_iteration):
        regret_instantane = bandit_aleatoire.baseline_aleatoire(rec_moy_est,nb_fois)
        if i==0:
            regret_cumule[i] = regret_instantane
        else:
            regret_cumule[i] = regret_cumule[i - 1] + regret_instantane

    # Tracer le regret en fonction du temps
    plt.figure(f"Graph regret baseline_aleatoire en fonction du temps")
    plt.plot(temps,regret_cumule, label="Baseline_aléatoire")
    plt.xlabel("Temps")
    plt.ylabel("Regret cumulé")
    plt.legend()
    plt.show()


def data_greedyAlgorithmn(nombre_iteration,jeu):
    """
    Effectue des simulations avec un bandit manchot utilisant la stratégie "greedy".

    Args:
        nombre_iteration (int): Le nombre d'itérations pour les simulations.
    """
    
    bandit_aleatoire = BanditManchot(jeu)
    rec_moy_est =  [0.0] * len(jeu.colonne_disponible())
    nb_fois =  [0]* len(jeu.colonne_disponible())
    temps = np.arange(nombre_iteration)
    regret_cumule = np.zeros(nombre_iteration)

    for i in range(nombre_iteration):
        regret_instantane = bandit_aleatoire.greedy_algorithm(rec_moy_est,nb_fois)
        if i==0:
            regret_cumule[i] = regret_instantane
        else:
            regret_cumule[i] = regret_cumule[i - 1] + regret_instantane

    # Tracer le regret en fonction du temps
    plt.figure(f"Graph regret greedyAlgo en fonction du temps")
    plt.plot(temps,regret_cumule, label="greedyAlgorithmn")
    plt.xlabel("Temps")
    plt.ylabel("Regret cumulé")
    plt.legend()
    plt.show()


def data_egreedy(nombre_iteration,epsilon,jeu):
    """
    Effectue des simulations avec un bandit manchot utilisant la stratégie "epsilon-greedy".

    Args:
        nombre_iteration (int): Le nombre d'itérations pour les simulations.
        epsilon (float): Le paramètre epsilon pour la stratégie epsilon-greedy.
    """

    bandit_aleatoire = BanditManchot(jeu)
    rec_moy_est =  [0.0] * len(jeu.colonne_disponible())
    nb_fois =  [0]* len(jeu.colonne_disponible())
    temps = np.arange(nombre_iteration)
    regret_cumule = np.zeros(nombre_iteration)

    for i in range(nombre_iteration):
        regret_instantane = bandit_aleatoire.e_greedy(epsilon,rec_moy_est,nb_fois)
        if i==0:
            regret_cumule[i] = regret_instantane
        else:
            regret_cumule[i] = regret_cumule[i - 1] + regret_instantane

    # Tracer le regret en fonction du temps
    plt.figure(f"Graph regret E-greedy en fonction du temps")
    plt.plot(temps,regret_cumule, label="E-greedy")
    plt.xlabel("Temps")
    plt.ylabel("Regret cumulé")
    plt.legend()
    plt.show()

def data_ucb(nombre_iteration,jeu):
    """
    Effectue des simulations avec un bandit manchot utilisant la stratégie "Upper Confidence Bound (UCB)".

    Args:
        nombre_iteration (int): Le nombre d'itérations pour les simulations.
    """
    
    bandit_aleatoire = BanditManchot(jeu)
    
    rec_moy_est =  [0.0] * len(jeu.colonne_disponible())
    nb_fois =  [0]* len(jeu.colonne_disponible())
    temps = np.arange(nombre_iteration)
    regret_cumule = np.zeros(nombre_iteration)

    for i in range(nombre_iteration):
        regret_instantane = bandit_aleatoire.ucb(rec_moy_est,nb_fois)
        if i==0:
            regret_cumule[i] = regret_instantane
        else:
            regret_cumule[i] = regret_cumule[i - 1] + regret_instantane

    # Tracer le regret en fonction du temps
    plt.figure(f"Graph regret UCB en fonction du temps")
    plt.plot(temps,regret_cumule, label="UCB")
    plt.xlabel("Temps")
    plt.ylabel("Regret cumulé")
    plt.legend()
    plt.show()

