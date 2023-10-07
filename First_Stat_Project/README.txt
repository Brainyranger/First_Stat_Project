Question 1.4:
   En observant le graphique de densité et l'histogramme pour un grand nombre de parties (1000), il semble que la distribution suive une loi binomiale. Cette conclusion est basée sur le fait que chaque partie est traitée comme une expérience indépendante dans des conditions similaires, et que chaque joueur joue de manière aléatoire. On peut considérer chaque partie comme une variable aléatoire suivant une loi binomiale, avec les paramètres p (probabilité de victoire) et n (nombre de coups jusqu'à la victoire).

Question 1.5:
   D'un point de vue mathématique, la probabilité qu'un joueur gagne peut être exprimée comme la somme des probabilités des deux événements élémentaires : A (joueur 1 gagne) et B (joueur 2 gagne). Ainsi, p (probabilité de victoire) = p(A) + p(B), et la probabilité d'un match nul est donnée par 1 - p.

   D'un point de vue informatique, pour calculer la probabilité de victoire de chaque joueur, il suffit de compter le nombre de victoires de chaque joueur et de diviser par le nombre total de parties jouées. Ensuite, la probabilité d'un match nul peut être calculée en soustrayant la somme des probabilités de victoire des joueurs à 1.

Question 1.6:
   Pour déterminer la probabilité de victoire de chaque joueur, nous pouvons d'abord estimer le nombre de possibilités de victoire pour chaque joueur. Étant donné que les joueurs jouent au hasard, la probabilité serait similaire pour les deux joueurs. Par application numérique, on peut estimer la probabilité de victoire, par exemple p(victoire) = (24 + 28 + 24) / (2 * 76) = 0,5. Sachant que 2 * p(victoire) + p(match nul) = 1, on peut déduire que la probabilité d'un match nul est proche de zéro.

Question 1.7:
   On peut donner une borne supérieure au nombre de parties différentes qui peuvent être jouées. Étant donné qu'il y a 42 emplacements sur le plateau, et chaque emplacement peut être rempli ou non, la borne supérieure théorique serait de 2^42 parties différentes. Pour obtenir une estimation plus précise, il serait nécessaire de fournir une stratégie unique à chaque joueur pour chaque partie, ce qui permettrait de déterminer combien de parties uniques ont été jouées lors de l'expérience.

Question 1.8:
   En ce qui concerne les algorithmes de bandit manchot, nous observons que les algorithmes gloutons (greedy) et les algorithmes aléatoires sont similaires dans la mesure où ils ne tiennent pas compte des informations sur les actions précédentes. Par conséquent, ils peuvent choisir des actions non optimales de manière fréquente. L'algorithme glouton est légèrement plus performant car il exploite les informations qu'il a à chaque étape, mais à long terme, il peut également être peu efficace comme l'algorithme aléatoire.

   Parmi les algorithmes étudiés, deux se démarquent comme étant plus performants. Tout d'abord, l'algorithme ε-greedy permet de choisir entre l'exploitation des données actuelles et l'exploration d'autres actions pour rechercher une meilleure solution. Il s'agit d'une amélioration de l'algorithme glouton.

   L'algorithme UCB (Upper Confidence Bound) se distingue comme le meilleur choix, car il parvient à équilibrer efficacement l'exploration et l'exploitation. Il analyse les données pour choisir judicieusement les actions à entreprendre tout en explorant de nouvelles possibilités lorsque nécessaire.



Programme de Simulation de Jeu:
   Ce programme a été développé pour effectuer des simulations et des comparaisons pour un jeu. Il propose plusieurs fonctionnalités pour étudier différents aspects du jeu, notamment des stratégies de joueur, des analyses de bandits manchots, et des comparaisons entre différentes approches.*

Utilisation:
   Exécutez le fichier main.py pour lancer le programme.
   Le menu principal s'affichera avec plusieurs options, dont les principales sont :
      - Aléatoire
      - Bandit Manchot
      - Monte Carlo
      - UCT
      - Comparaison Exploration Exploitation Équilibré
      - Quitter le programme
   Sélectionnez l'option qui vous intéresse en entrant le numéro correspondant.
   Suivez les instructions pour exécuter la simulation ou l'analyse souhaitée.

Options de Menu:
 Aléatoire: Exécute des simulations aléatoires pour le jeu.
 Bandit Manchot: Vous permet de choisir entre différentes stratégies de bandit manchot et d'effectuer des analyses.
   - Greedy
   - e_Greedy
   - UCB
 Monte Carlo: Effectue des simulations et des comparaisons impliquant l'algorithme Monte Carlo.
   - Monte Carlo vs Aleatoire
   - Monte Carlo vs Monte Carlo
 UCT: Effectue des simulations et des comparaisons impliquant l'algorithme UCT (Upper Confidence Bound for Trees).
   - UCT vs Aleatoire
   - UCT vs Monte Carlo
 Comparaison Exploration Exploitation Équilibré: Compare différentes stratégies d'exploration et d'exploitation.
   - Greedy vs e_Greedy
   - UCB vs Greedy
   - UCB vs e_Greedy
   - UCB vs UCT

Configuration du Jeu:
   Le programme est configuré pour utiliser un plateau de jeu, deux joueurs, et différentes constantes. Vous pouvez personnaliser ces paramètres en modifiant les variables correspondantes dans le code.
