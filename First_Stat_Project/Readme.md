Tutoriel pour l'éxécution du main : 

Lancez : 

python main.py (sous windows)

python3 main.py (sous linux) 


Vous aurez des choix présentés sur le terminal : 

|-- 1. Aléatoire
|-- 2. Bandit Manchot
|-- 3. Monte Carlo
|-- 4. UCT
|-- 5. Comparaison Exploration Exploitation Equilibré
|-- 6. Exit

L'utilisateur peut choisir différentes options : 

S'il choisit "Aléatoire" (option 1), il exécute une expérience spécifique.

S'il choisit "Bandit Manchot" (option 2), il accède à un sous-menu pour choisir une variante du jeu :
Bandit Manchot
|-- 1. Baseline Aleatoire
|-- 2. Greedy
|-- 3. eGreedy
|-- 4. UCB


S'il choisit "Monte Carlo" (option 3), il accède à un sous-menu pour choisir entre deux expériences Monte Carlo : 
Monte Carlo
|-- 1. Monte Carlo vs Aléatoire
|-- 2. Monte Carlo vs Monte Carlo

S'il choisit "UCT" (option 4), il accède à un sous-menu pour choisir entre deux expériences UCT : 
UCT
|-- 1. UCT vs Aléatoire
|-- 2. UCT vs Monte Carlo

S'il choisit "Comparaison Exploration Exploitation Equilibré" (option 5), il accède à un sous-menu pour choisir entre différentes comparaisons : 
Comparaison Exploration Exploitation Equilibré
|-- 1. Greedy vs e_Greedy
|-- 2. UCB vs Greedy
|-- 3. UCB vs e_Greedy
|-- 4. UCB vs UCT

S'il choisit "Exit" (option 6), le programme se termine.
