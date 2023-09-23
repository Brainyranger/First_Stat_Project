import numpy as np
from Constante import NOMBRE_LEVIERS


class BanditManchot:

    def __init__(self):
        self.rec_moy_est =  [0.0] * NOMBRE_LEVIERS
        self.nb_fois =  [0]* NOMBRE_LEVIERS
        self.temps_total = 0
        self.probabilites_succes = [np.random.uniform(0, 1) for _ in range(NOMBRE_LEVIERS)]


    
    def gain_bernoulli(self,leviers, action_choisie):
        if action_choisie < 0 or action_choisie >= len(leviers):
            raise ValueError("L'action choisie est invalide.")
    
        parametre_bernoulli = leviers[action_choisie]
        resultat_tirage = np.random.random()  
        print(leviers)
        if resultat_tirage <= parametre_bernoulli:
            return 1  
        else:
            return 0  

    def baseline_aleatoire(self):
        action_choisie = np.random.choice(range(0, len(self.rec_moy_est)))
        recompense = self.gain_bernoulli(self.probabilites_succes,action_choisie)


        self.nb_fois[action_choisie] += 1
        self.rec_moy_est[action_choisie] = (self.rec_moy_est[action_choisie] * (self.nb_fois[action_choisie] - 1) + recompense) / self.nb_fois[action_choisie]
       

        return action_choisie

    def greedy_algorithm(self):
        if np.min(self.rec_moy_est) == 0:
            return self.baseline_aleatoire()
    
        action_choisie = np.argmax(self.rec_moy_est)
        
        recompense = self.gain_bernoulli(self.probabilites_succes,action_choisie)
     

        self.nb_fois[action_choisie] += 1
        self.rec_moy_est[action_choisie] = (self.rec_moy_est[action_choisie] * (self.nb_fois[action_choisie] - 1) + recompense) / self.nb_fois[action_choisie]
    
    
        return recompense


    def e_greedy(self,epsilon):
    
        while True:
            if np.random.random() < epsilon:
                return self.baseline_aleatoire()
            else:
                break
                
        action_choisie = np.argmax(self.rec_moy_est)
        
        recompense = self.gain_bernoulli(self.probabilites_succes,action_choisie) 

        self.nb_fois[action_choisie] += 1
        self.rec_moy_est[action_choisie] = (self.rec_moy_est[action_choisie] * (self.nb_fois[action_choisie] - 1) + recompense) / self.nb_fois[action_choisie]
    
        return recompense



    def ucb(self):
        ucb_values = np.zeros(NOMBRE_LEVIERS)
        action_choisie = 0
        exploitation_term = 0
        exploration_term = 0
        for i in range(NOMBRE_LEVIERS):
            if self.nb_fois[i] == 0:
                action_choisie = i
            else:
                exploitation_term = self.rec_moy_est[i]
                exploration_term = np.sqrt(2 * np.log(self.temps_total) / self.nb_fois[i])
                ucb_values[i] = exploitation_term + exploration_term
               
      
        action_choisie = np.argmax(ucb_values)
        recompense = self.gain_bernoulli(self.probabilites_succes,action_choisie)
        self.nb_fois[action_choisie] += 1
        self.temps_total += 1
        self.rec_moy_est[action_choisie] = (self.rec_moy_est[action_choisie] * (self.nb_fois[action_choisie] - 1) + recompense) / self.nb_fois[action_choisie]

        return recompense

    def reset_action(self):
        self.rec_moy_est =  [0.0] * NOMBRE_LEVIERS
        self.nb_fois =  [0]* NOMBRE_LEVIERS
        self.temps_total = 0