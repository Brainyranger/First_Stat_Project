Question 1.4)

En observant le graphique de densité et l'histogramme sur un nombre de partie à grande échelle(1000).
On en déduit que la distribution suit une loi binomiale, en effet les expériences de chaque parti sont traitées
de manière indépendantes dans les mêmes conditions. De plus il y a on a une equiprobalité pour chaque joueur car il joue 
d'une manière aléatoire. On suppose le cas d'un match obsolète. On peut donc déduire que que chaque parti suit une loi 
binomiale B de paramètre :  p = p(victoire), n = nb_coup jusqu'à la victoire.


Question 1.5) 

Point de vue mathématique : 

Soit p une probabilité d'avoir un joueur gagnant 
Soit A,B deux événements élémentaires tels que  A : joueur 1 gagne et B : joueur 2 gagne 
la probabilité d'avoir un joueur gagnant est donc de p = p(A)+p(B)
la probabilité d'avoir match nulle est donc non(p)= 1-p 

Point de vue informatique : 

Il suffit premièrement de calculer pour une parti quelle est la probabilité pour que la joueur A gagne (resp. B).
Pour cela compter le nombre de victoire de A(resp.B) puis diviser cela par le nombre de partie jouée.
Puis de faire la somme de des probabilité de victoire de A et B puis le soustraire à 1.

Question 1.6)

L'idée est de partir sur le chemin opposé. On détermine d'abord la probabilité de victoire pour chaque joueur (vue qu'ils jouent au hasard la probabilité serait similaire)
On sait que p(victoire) = (nb_possibilité_victoire_joueur)/nb_possibilité_victoire
Par application numérique on aura p(victoire) = (24+28+24)/2*76 = 0.5
Sachant que 2*p(victoire)+p(nulle)=1 donc on en déduit que p(nulle) peut être borné à zéro ou relativement proche.

Question 1.7)

On peux donner une borne supérieur aux nombres de parties différentes qui peuvent être joués. En effet le plateau à 42 emplacements. 
Chaque emplacement peut être rempli ou non. Donc on en conclut que la borne supérieur théorqiue est de 2^42 partie différentes.
L'expérience que nous pourrons donner c'est d'octroyer à chaque joueur une stratégie. Pour chaque partie le joueur aura une nouvelle stratégie.
Cela la nous permettrait d'avoir avec plus de précision combien de parties uniques il y a eu durant l'expérience.

Question 1.8)

 

