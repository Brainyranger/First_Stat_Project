# Mohamed Elyes Bourenane
# David Kitoko

from utils import *

import pandas as pd
import numpy as np

def getPrior(data):
    """
        Calculer la probabilité a priori de la classe $1$ ainsi que l'intervalle de confiance à 95% pour l'estimation de cette probabilité.
        Parametes
        ---------
            data : pandas.dataframe
                le `pandas.dataframe` contenant les données
        
        Returns
        ---------
            Dict[str,float]
                un dictionnaire incluant l'estimation, min5pourcent, max5pourcent
    """

    moyenne = data["target"].sum() / len(data["target"])
    ecart_type = (moyenne - moyenne**2)**0.5 / len(data["target"])**0.5
    print(ecart_type)

    return {"estimation": moyenne, "min5pourcent": moyenne - 1.96 * ecart_type, "max5pourcent": moyenne + 1.96 * ecart_type}

class APrioriClassifier(AbstractClassifier):
    def __init__(self):
        self.est_dict = getPrior(data)

