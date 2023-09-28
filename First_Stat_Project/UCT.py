import numpy as np
from Node import Node
from BanditManchot import BanditManchot

class UCT:
    """
        Cette classe représente un arbre UCT (arbre d'expolation) désigne l’algorithme UCB adapté aux arbres de jeu (communément appelé également
        Monte Carlo Tree Search)

        Args:
            jeu (objet de Jeu): L'objet de jeu sur lequel le joueur effectue son coup.
            joueur (objet de Joueur): L'objet de joueur qui va jouer le prochain coup.
        
        Attributs:
            racine: (objet de Node): le noeud qui représente la racine de l'arbre UCT

        Methodes:
            is_fully_expanded(node): verifie si tous les enfants possible ont été crées
            select_child(node): Selectionner un noeud à explorer à partir de noeud node en fonction de l'algorithme UCB
            expand(node): Creer un noeud et le simuler pour une action jamais effectuée au noeud node
            simulate(node):  à partir d’un nœud à simuler, un jeu entre deux joueurs aléatoires est déroulé jusqu’à atteindre un état final
            backpropagate(node, result): Mettre à jour en fonction du résultat le nombre de victoires et le nombre de visites pour chaque noeud
            play_uct(iterations): Simulation de l'algorithme UCT pour itérations fois
    """
    def __init__(self, jeu, joueur):
        """
            Initialise un arbre UCT par la création de sa racine
        """
        self.racine = Node(jeu, joueur)
        self.racine.racine = True


    def is_fully_expanded(self, node):
        """
            Verifie si tous les enfants possible ont été crées

            Args:
                node (objet de Node): le noeud courant dans l'arbre

            Returns:
                (boolean): True si tous les enfants du noeud ont été crées pour touts les colonnes disponobiles
        """

        return len(node.enfants) == len(node.jeu.colonne_disponible())
    
    def select_child(self, node):
        """
            Selectionner un noeud à explorer à partir de noeud node en fonction de l'algorithme UCB

            Args:
                node (objet de Node): le noeud courant dans l'arbre

            Returns:
                (Node): le noeud fils selectionné
        """

        nb_fois = np.array([child.nb_visite for child in node.enfants])
        rec_moy_est = np.array([node.enfants[i].nb_gagne / nb_fois[i] for i in range(len(node.enfants))])

        bandit_alea = BanditManchot(node.jeu)
        best_child = bandit_alea.ucb_return_action(rec_moy_est, nb_fois)

        return node.enfants[best_child]
    
    def expand(self, node):
        """
            Creer un noeud et le simuler pour une action jamais effectuée au noeud node

            Args:
                node (objet de Node): le noeud courant dans l'arbre

            Returns:
                (Node): le noeud créé ou le noeud séléctionné si toutes les actions ont été effectué
        """
        actions_possibles = np.array(node.jeu.colonne_disponible())
        actions_pas_explores = np.array([action for action in actions_possibles if not any(child.action == action for child in node.enfants)])
        if len(actions_pas_explores) > 0:
            action = np.random.choice(actions_pas_explores)
            child_jeu = node.jeu.copie()
            child_jeu.play(action, node.joueur)
            child = Node(child_jeu, node.joueur, parent=node, action=action)
            node.enfants.append(child)
            return child
        else:
            return self.select_child(node)
        
    def simulate(self, node):
        """
            A partir d’un nœud à simuler, un jeu entre deux joueurs aléatoires est déroulé jusqu’à atteindre un état final

            Args:
                node (objet de Node): le noeud courant dans l'arbre

            Returns:
                (int): l'identifiant du joueur gagnant aprés la simulation
        """

        jeu_copie = node.jeu.copie()
        joueur_actuel = node.joueur
        
        while not jeu_copie.is_finished():
            action = np.random.choice(jeu_copie.colonne_disponible())
            jeu_copie.play(action, joueur_actuel)
            if joueur_actuel.id_joueur == jeu_copie.j1.id_joueur:
                joueur_actuel = jeu_copie.j2
            else:
                joueur_actuel = jeu_copie.j1

        if jeu_copie.gagnant == node.joueur:
            return 1
        elif jeu_copie.gagnant == 0:
            return 0
        else:
            return -1
        
    def backpropagate(self, node, result):
        """
            Mettre à jour en fonction du résultat le nombre de victoires et le nombre de visites pour chaque noeud

            Args:
                node (objet de Node): le noeud courant dans l'arbre
                result (int): l'identifiant du joueur gagnant 
        """
        while node is not None:
            node.nb_visite += 1
            if node.joueur.id_joueur == result:
                node.nb_gagne += 1
            node = node.parent

    def play_uct(self, iterations):
        """
            Simulation de l'algorithme UCT pour itérations fois

            Args:
                iterations(int): nombre de simulation

            Returns:
                (int): L'indice de la colonne choisie en utilisant la méthode UCT
        """
        for _ in range(iterations):
            node = self.racine
            while not node.jeu.is_finished():
                if not self.is_fully_expanded(node):
                    node = self.expand(node)
                else:
                    node = self.select_child(node)

                if len(node.enfants) == 0:
                    break
            
            result = self.simulate(node)
            self.backpropagate(node, result)

        best_child = max(self.racine.enfants, key=lambda child: child.nb_visite)

        return best_child.action
