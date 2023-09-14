import numpy as np

class Plateau:
    def __init__(self, nb_ligne, nb_colonne):
        self.nb_ligne = nb_ligne
        self.nb_colonne = nb_colonne
        self.tableau = self.tableau = np.zeros((self.nb_ligne, self.nb_colonne), dtype=int)
    

    def liste_succes(self):
        liste = []

        # vertical
        for i in range(0, self.nb_colonne):
            j = 0
            while j + 3 < self.nb_ligne:
                liste.append([(j, i), (j + 1, i), (j + 2, i), (j + 3, i)])
                j += 1
        

        # horizontal
        for i in range(0, self.nb_ligne):
            j = 0
            while j + 3 < self.nb_colonne:
                liste.append([(i, j), (i, j + 1), (i, j + 2), (i, j + 3)])
                j += 1

        # diagonal
        for i in range(0, self.nb_ligne):
            if self.nb_ligne - i < 4 :
                break

            j = 0
            while j + 3 < self.nb_colonne:
                liste.append([(i, j), (i + 1, j + 1), (i + 2, j + 2), (i + 3, j + 3)])
                j += 1

        for i in range(self.nb_ligne - 1, 0, -1):
            if i - 3 < 0 :
                break

            j = 0
            while j + 3 < self.nb_colonne:
                liste.append([(i, j), (i - 1, j + 1), (i - 2, j + 2), (i - 3, j + 3)])
                j += 1

        return liste    
        
#p = Plateau(6, 7)

# p.reset()
#print(p.tableau)

#print(p.liste_succes())