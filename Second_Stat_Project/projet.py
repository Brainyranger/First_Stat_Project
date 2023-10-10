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

    return {"estimation": moyenne, "min5pourcent": moyenne - 1.96 * ecart_type, "max5pourcent": moyenne + 1.96 * ecart_type}

class APrioriClassifier(AbstractClassifier):
    def __init__(self):
        self.prop_apriori = 0

    def estimClass(self, attrs):
        """
        à partir d'un dictionanire d'attributs, estime la classe 0 ou 1

        Parameters
        ---------
        attr: Dict[str,val] 
            Le dictionnaire nom-valeur des attributs

        Returns
        -------
        la classe 0 ou 1 estimée
        """
        return 1 if self.prop_apriori >= 0.5 else 0
    
    def statsOnDF(self, df):
        """
        à partir d'un pandas.dataframe, calcule les taux d'erreurs de classification et rend un dictionnaire.

        Parameters
        ----------
        df:  pandas.DataFram
            le dataframe à tester
        
        Returns
        -------
        Dict[str,float]
            un dictionnaire incluant les VP,FP,VN,FN,précision et rappel
        """

        VP = 0
        VN = 0
        FP = 0
        FN = 0

        self.prop_apriori = getPrior(df)["estimation"]

        for i in range(len(df)):
            dic = getNthDict(df, i)
            classe_predite = self.estimClass(dic)

            if dic["target"] == 1:
                if classe_predite == 1:
                    VP += 1
                else:
                    FN += 1
            else:
                if classe_predite == 1:
                    FP += 1
                else:
                    VN += 1
        
        precision = VP / (VP + FP) if (VP + FP) > 0 else 0
        rappel = VP / (VP + FN) if (VP + FN) > 0 else 0

        return {'VP': VP, 'VN': VN, 'FP': FP, 'FN': FN, 'Précision': precision, 'Rappel': rappel}
    
def P2D_l(df, attr):
    """
        calcule dans le dataframe la probabilité  P(attr|target)

        Parameters
        ----------
        df:  pandas.DataFram
            le dataframe à tester
        attr: string
            le nom de la colonne
        
        Returns
        -------
        Dict[int,float]
            un dictionnaire de la loi de probabilité P(attr|target)
    """
    probabilites = {}
    unique_targets = df['target'].unique()

    for target_value in unique_targets:
        filtered_df = df[df["target"] == target_value]

        nb_attr = filtered_df[attr].value_counts().to_dict()

        nb_total = len(filtered_df)

        probabilites[target_value] = {attr_value: count / nb_total for attr_value, count in nb_attr.items()}

    return probabilites

def P2D_p(df,attr):
    """
        calcule dans le dataframe la probabilité  P(target|attr)

        Parameters
        ----------
        df:  pandas.DataFram
            le dataframe à tester
        attr: string
            le nom de la colonne
        
        Returns
        -------
        Dict[int,float]
            un dictionnaire de la loi de probabilité P(target|attr)
    """

    probabilites = {}
    unique_attr = df[attr].unique()

    for attr_value in unique_attr:
        filtered_df = df[df[attr] == attr_value]

        nb_target = filtered_df["target"].value_counts().to_dict()

        nb_total = len(filtered_df)

        probabilites[attr_value] = {target_value : count / nb_total for target_value, count in nb_target.items()}

    return probabilites

class ML2DClassifier(APrioriClassifier):
    def __init__(self, df, attr):
        super().__init__
        self.attr = attr
        self.P2D_l = P2D_l(df, attr)

    def estimClass(self, attrs):
        if self.attr in attrs:
            attr_value = attrs[self.attr]
            max_likehood = max(self.P2D_l.keys(), key=lambda target: self.P2D_l[target].get(attr_value, 0))
            return max_likehood
        return 0


class MAP2DClassifier(APrioriClassifier):
    def __init__(self, df, attr):
        super().__init__()
        self.attr = attr
        self.P2Dp = P2D_p(df,attr)

    

    def estimClass(self, attributs):
        if self.attr in attributs:
            attr_value = attributs[self.attr]            
            max_posterior_class = max(self.P2Dp[attr_value].keys(), key=lambda target: self.P2Dp[attr_value].get(target, 0))
            return max_posterior_class

        return 0
    
#####
# Question 2.4 : comparaison
#####

# 1. **APrioriClassifier** :
#    - Précision en validation : 0.69
#    - Rappel en validation : 1.0

#    Ce classifieur a une précision modérée en validation, ce qui signifie qu'il peut donner un grand nombre de faux positifs (FP) par rapport aux vrais positifs (VP). Cependant, il a un rappel élevé, ce qui signifie qu'il capture correctement tous les vrais positifs, mais au détriment d'un nombre plus élevé de faux positifs.

# 2. **ML2DClassifier (Maximum Likelihood)** :
#    - Précision en validation : 0.8898
#    - Rappel en validation : 0.8188

#    Le ML2DClassifier montre une amélioration significative de la précision par rapport à l'APrioriClassifier en validation, réduisant ainsi le nombre de faux positifs. Cependant, le rappel a légèrement diminué, ce qui signifie qu'il pourrait manquer certains vrais positifs.

# 3. **MAP2DClassifier (Maximum A Posteriori)** :
#    - Précision en validation : 0.8571
#    - Rappel en validation : 0.8261

#    Le MAP2DClassifier se situe entre l'APrioriClassifier et le ML2DClassifier en termes de précision. Il offre un bon équilibre entre la réduction des faux positifs et le maintien d'un rappel décent.

# Si on souhaite minimiser les faux positifs, le ML2DClassifier peut être préférable en raison de sa meilleure précision. Si on souhaite maintenir un bon équilibre entre la précision et le rappel, le MAP2DClassifier pourrait être un bon choix.
#####
