import numpy as np
import matplotlib.pyplot as plt
from Jeu import Jeu
from Plateau import Plateau
from Joueur import Joueur


def data_run(title, joueur1, joueur2, plateau, nb_parts=100):
    """ Lance une partie entre 2 joueurs et etudie le nombre de coup jusqu'à une victoire, pour le joueur 1 et pour le joueur 2 """

   
    jeu = Jeu(plateau,joueur1,joueur2)
    for i in range(nb_parts):
        gagnat = jeu.run() 
        if jeu.gagnant == joueur1.id_joueur:
            plt.scatter([jeu.j1.nb_parti_gagner],i,color="blue", linestyle = "solid",label="Winner 1")
        if jeu.gagnant == joueur2.id_joueur:
            plt.scatter([jeu.j1.nb_parti_gagner],i,color="red",linestyle = "solid", label="Winner 2")

        #jeu.reset()

  

    print(title)
    print("Nb parties nulles\t:", jeu.j1.nb_parti_egalite)
    print("Nb parties gagnées joueur 1\t:", jeu.j1.nb_parti_gagner)
    print("Nb parties gagnées joueur 2\t:", jeu.j2.nb_parti_gagner)


    plt.title(f"{title} Joueur 1 vs Joueur 2")
    plt.ylabel("Nb victoires")
    plt.xlabel("Nb Coups")
    plt.grid(True)
    #plt.legend()
    plt.show()



#p = Plateau(6,7)
#j1 = Joueur(1,21)
#j2 = Joueur(-1,21)
#data_run("data_experimental",j1,j2,p,100)
