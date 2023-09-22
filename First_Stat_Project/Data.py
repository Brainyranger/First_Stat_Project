import numpy as np
import matplotlib.pyplot as plt
from Jeu import Jeu
from Plateau import Plateau
from Constante import NB_JETON
from Joueur import Joueur
from scipy.stats import kde




def data_run(title, joueur1, joueur2, plateau, nb_parts):
    """ Lance une partie entre 2 joueurs et etudie le nombre de coup jusqu'à une victoire, pour le joueur 1 et pour le joueur 2 """


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
    plt.figure(f"{title}")
    plt.hist(np.array(res_joueur1),bins=25,label="joueur 1")
    plt.hist(np.array(res_joueur2),bins=25,label="joueur 2")
    plt.ylabel("Nb victoires")
    plt.xlabel("Nb Coups")

    #trace le graphique de densite
    density_1 = kde.gaussian_kde(np.array(res_joueur1))
    density_2 = kde.gaussian_kde(np.array(res_joueur2))
    x = np.linspace(4,20,300)
    y1 = density_1(x)
    y2 = density_2(x) 
    #plt.plot(x,y1,label="joueur 1")
    #plt.plot(x,y2,label="joueur 2")
    #plt.ylabel("Densité")
    #plt.xlabel("Nombre de Coups")
    
    
    plt.legend()
    plt.grid()
    plt.show()
   



