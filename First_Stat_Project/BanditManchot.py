import numpy as np



class BanditManchot:
    """
    Cette classe représente un bandit manchot, un problème classique en apprentissage par renforcement où un agent doit
    choisir parmi plusieurs leviers pour maximiser sa récompense cumulée.

    Args:
        nombre_leviers (int): Le nombre de leviers disponibles dans le bandit.

    Attributes:
        nombre_leviers (int): Le nombre de leviers dans le bandit.
        probabilites_succes (numpy.ndarray): Les probabilités de succès de chaque levier.
        estimations_moyennes (numpy.ndarray): Les estimations moyennes de la récompense pour chaque levier.
        nombre_tirages (numpy.ndarray): Le nombre de fois que chaque levier a été tiré.

    Methods:
        tirer_levier(levier): Tire un levier spécifique et retourne la récompense obtenue.
        action_baseline_aleatoire(): Choix d'action aléatoire selon la stratégie "baseline aléatoire".
        action_greedy(): Choix d'action selon la stratégie "greedy".
        action_epsilon_greedy(epsilon): Choix d'action selon la stratégie "epsilon-greedy".
        action_ucb(): Choix d'action selon la stratégie "Upper Confidence Bound (UCB)".

    """



    def __init__(self,jeu):
        """
        Initialise un bandit manchot.

        Le bandit manchot a plusieurs leviers, chacun avec une probabilité de succès aléatoire.

        Attributes:
            rec_moy_est (list): Liste des estimations de récompense moyenne pour chaque levier.
            nb_fois (list): Nombre de fois que chaque levier a été actionné.
            temps_total (int): Nombre total d'actions effectuées sur le bandit.
            probabilites_succes (list): Liste des probabilités de succès pour chaque levier.
        """

        self.temps_total = 0
        self.nombre_leviers = jeu.colonne_disponible()
        self.probabilites_succes = [np.random.uniform(0, 1) for _ in range(len(self.nombre_leviers))]


    
    def gain_bernoulli(self,leviers, action_choisie):
        """
        Simule un gain selon une distribution de Bernoulli pour une action choisie.

        Args:
            leviers (list): Liste des probabilités de succès pour chaque levier.
            action_choisie (int): L'indice de l'action choisie.

        Returns:
            int: Le gain (1 ou 0) de l'action choisie.
        """

        if action_choisie < 0 or action_choisie >= len(leviers):
            raise ValueError("L'action choisie est invalide.")
    
        parametre_bernoulli = leviers[action_choisie] #choisie la probabilité de succés d'un levier à l'indice action_choisie
        resultat_tirage = np.random.random()  #choisi  un nombre aléatoire entre 0 et 1 exclus

        if resultat_tirage <= parametre_bernoulli: #on vérifie que le tirage aléatoire réussit 
            return 1  
        else:
            return 0  

    def baseline_aleatoire(self, rec_moy_est, nb_fois):
        """
        Applique la stratégie de sélection d'action aléatoire (baseline aléatoire).

        Args:
        rec_moy_est (list): Liste des estimations de récompenses moyennes pour chaque action.
        nb_fois (list): Liste des compteurs d'action pour chaque action.

        Returns:
        int: L'indice de l'action choisie de manière aléatoire.

        Note:
        Cette méthode met à jour les estimations de récompenses moyennes, les compteurs d'action.

        """

        action_choisie = np.random.choice(range(0, len(rec_moy_est))) #choisi une action disponible 
        recompense = self.gain_bernoulli(self.probabilites_succes,action_choisie) # on détermine la récompense associé à l'action

        #update 
        nb_fois[action_choisie] += 1
        rec_moy_est[action_choisie] = (rec_moy_est[action_choisie] * (nb_fois[action_choisie] - 1) + recompense) / nb_fois[action_choisie]
       

        return action_choisie

    def greedy_algorithm(self, rec_moy_est, nb_fois):
        """
         Applique la stratégie de sélection d'action greedy (exploitation).

        Args:
        rec_moy_est (list): Liste des estimations de récompenses moyennes pour chaque action.
        nb_fois (list): Liste des compteurs d'action pour chaque action.

        Returns:
        int: Le gain (1 ou 0) de l'action choisie.

        Note:
        Cette méthode met à jour les estimations de récompenses moyennes, les compteurs d'action.

        """

        if np.min(rec_moy_est) == 0:#on vérfie si il nous reste des actions à explorer
            return self.baseline_aleatoire(rec_moy_est,nb_fois)
    
        action_choisie = np.argmax(rec_moy_est)# on choisi l'action avec le plus de récompenses en moyenne 
        
        recompense = self.gain_bernoulli(self.probabilites_succes,action_choisie)#on détermine la récompense associé à l'action
     
        #update
        nb_fois[action_choisie] += 1
        rec_moy_est[action_choisie] = (rec_moy_est[action_choisie] * (nb_fois[action_choisie] - 1) + recompense) /nb_fo is[action_choisie]
    
    
        return recompense

    def greedy_algorithm_return_action(self, rec_moy_est, nb_fois):
        """
         Applique la stratégie de sélection d'action greedy (exploitation).

        Args:
        rec_moy_est (list): Liste des estimations de récompenses moyennes pour chaque action.
        nb_fois (list): Liste des compteurs d'action pour chaque action.

        Returns:
        int:  l'action choisie.

        Note:
        Cette méthode met à jour les estimations de récompenses moyennes, les compteurs d'action.

        """

        if np.min(rec_moy_est) == 0:#on vérfie si il nous reste des actions à explorer
            return self.baseline_aleatoire(rec_moy_est,nb_fois)
    
        action_choisie = np.argmax(rec_moy_est)# on choisi l'action avec le plus de récompenses en moyenne 
        
        recompense = self.gain_bernoulli(self.probabilites_succes,action_choisie)#on détermine la récompense associé à l'action
     
        #update
        nb_fois[action_choisie] += 1
        rec_moy_est[action_choisie] = (rec_moy_est[action_choisie] * (nb_fois[action_choisie] - 1) + recompense) /nb_fo is[action_choisie]
    
    
        return action_choisie



    def e_greedy(self,epsilon, rec_moy_est, nb_fois):
        """
        Applique la stratégie de sélection d'action epsilon-greedy.

        Args:
            epsilon (float): Le paramètre epsilon pour le choix de l'action.
            rec_moy_est (list): Liste des estimations de récompenses moyennes pour chaque action.
            nb_fois (list): Liste des compteurs d'action pour chaque action.

        Returns:
            int: Le gain (1 ou 0) de l'action choisie.

        Note:
        Cette méthode met à jour les estimations de récompenses moyennes, les compteurs d'action.

        """

        while True:
            if np.random.random() < epsilon:#On teste si on chosi l'action de manière aléatoire ou non
                return self.baseline_aleatoire(rec_moy_est,nb_fois)
            else:
                break
                
        action_choisie = np.argmax(rec_moy_est)# on choisi l'action avec le plus de récompenses en moyenne
        
        recompense = self.gain_bernoulli(self.probabilites_succes,action_choisie)#on détermine la récompense associé à l'action

        #update
        nb_fois[action_choisie] += 1
        rec_moy_est[action_choisie] = (rec_moy_est[action_choisie] * (nb_fois[action_choisie] - 1) + recompense) / nb_fois[action_choisie]
    
        return recompense

    def e_greedy_return_action(self,epsilon, rec_moy_est, nb_fois):
        """
        Applique la stratégie de sélection d'action epsilon-greedy.

        Args:
            epsilon (float): Le paramètre epsilon pour le choix de l'action.
            rec_moy_est (list): Liste des estimations de récompenses moyennes pour chaque action.
            nb_fois (list): Liste des compteurs d'action pour chaque action.

        Returns:
            int: l'action choisie.

        Note:
        Cette méthode met à jour les estimations de récompenses moyennes, les compteurs d'action.

        """

        while True:
            if np.random.random() < epsilon:#On teste si on chosi l'action de manière aléatoire ou non
                return self.baseline_aleatoire(rec_moy_est,nb_fois)
            else:
                break
                
        action_choisie = np.argmax(rec_moy_est)# on choisi l'action avec le plus de récompenses en moyenne
        
        recompense = self.gain_bernoulli(self.probabilites_succes,action_choisie)#on détermine la récompense associé à l'action

        #update
        nb_fois[action_choisie] += 1
        rec_moy_est[action_choisie] = (rec_moy_est[action_choisie] * (nb_fois[action_choisie] - 1) + recompense) / nb_fois[action_choisie]
    
        return  action_choisie



    def ucb(self, rec_moy_est, nb_fois):
        """
        Implémente la stratégie UCB (Upper Confidence Bound) pour choisir l'action à entreprendre.

        La méthode calcule les valeurs UCB pour chaque action, choisit l'action avec la plus grande valeur UCB et renvoie la récompense binaire associée à cette action.

        Args:
        rec_moy_est (list): Liste des estimations de récompenses moyennes pour chaque action.
        nb_fois (list): Liste des compteurs d'action pour chaque action.

        Returns:
        int: La récompense binaire (1 ou 0) de l'action choisie selon la stratégie UCB.

        Note:
        Cette méthode met à jour les estimations de récompenses moyennes, les compteurs d'action et le temps total.

        """
        ucb_values = np.zeros(len(self.nombre_leviers))
        action_choisie = 0
        exploitation_term = 0
        exploration_term = 0
        for i in range(0,len(self.nombre_leviers)):
            if nb_fois[i] == 0:#on vérifie qu'une action à déjà été choisi ou non
                action_choisie = i
            else:
                exploitation_term = rec_moy_est[i] #moyenne de recompense estimée pour l'action i 
                exploration_term = np.sqrt(2 * np.log(self.temps_total) / nb_fois[i])# formule UCB appliquée 
                ucb_values[i] = exploitation_term + exploration_term
               
      
        action_choisie = np.argmax(ucb_values)#on choisi la meilleur action 
        recompense = self.gain_bernoulli(self.probabilites_succes,action_choisie)#la récompense associé à la meilleur action

        #update
        nb_fois[action_choisie] += 1
        self.temps_total += 1
        rec_moy_est[action_choisie] = (rec_moy_est[action_choisie] * (nb_fois[action_choisie] - 1) + recompense) / nb_fois[action_choisie]

        return  recompense

    
    def ucb_return_action(self, rec_moy_est, nb_fois):
        """
        Implémente la stratégie UCB (Upper Confidence Bound) pour choisir l'action à entreprendre.

        La méthode calcule les valeurs UCB pour chaque action, choisit l'action avec la plus grande valeur UCB et renvoie la récompense binaire associée à cette action.

        Args:
        rec_moy_est (list): Liste des estimations de récompenses moyennes pour chaque action.
        nb_fois (list): Liste des compteurs d'action pour chaque action.

        Returns:
        int: l'action choisie selon la stratégie UCB.

        Note:
        Cette méthode met à jour les estimations de récompenses moyennes, les compteurs d'action et le temps total.

        """
        ucb_values = np.zeros(len(self.nombre_leviers))
        action_choisie = 0
        exploitation_term = 0
        exploration_term = 0
        for i in range(0,len(self.nombre_leviers)):
            if nb_fois[i] == 0:#on vérifie qu'une action à déjà été choisi ou non
                action_choisie = i
            else:
                exploitation_term = rec_moy_est[i] #moyenne de recompense estimée pour l'action i 
                exploration_term = np.sqrt(2 * np.log(self.temps_total) / nb_fois[i])# formule UCB appliquée 
                ucb_values[i] = exploitation_term + exploration_term
               
      
        action_choisie = np.argmax(ucb_values)#on choisi la meilleur action 
        recompense = self.gain_bernoulli(self.probabilites_succes,action_choisie)#la récompense associé à la meilleur action

        #update
        nb_fois[action_choisie] += 1
        self.temps_total += 1
        rec_moy_est[action_choisie] = (rec_moy_est[action_choisie] * (nb_fois[action_choisie] - 1) + recompense) / nb_fois[action_choisie]

        return  action_choisie

    
