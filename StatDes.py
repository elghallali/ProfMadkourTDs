import numpy as np


class StatDes:
    def __init__(self, dataSet):
        self.dataSet = dataSet

    def moyenne(self):
        return np.mean(self.dataSet)

    def variance(self):
        return np.var(self.dataSet)

    def ecartType(self):
        return np.sqrt(self.variance())

    def asymetrie(self):
        asy = [((i - self.moyenne()) / self.ecartType())**3 for i in self.dataSet]
        gamma1 = sum(asy) / len(self.dataSet)
        if gamma1 < -0.2:
            return f"le coefficient de Skewness = {gamma1:.4f}\ndonc la distribution est asymétrique à gauche"
        elif -0.2 <= gamma1 <= 0.2:
            return f"le coefficient de Skewness = {gamma1:.4f}\ndonc la distribution est symétrique"
        else:
            return f"le coefficient de Skewness = {gamma1:.4f}\ndonc la distribution est asymétrique à droite"

    def aplatissement(self):
        ap =[ ((i - self.moyenne()) / self.ecartType())**4 for i in self.dataSet]
        beta2 = sum(ap)/len(self.dataSet)
        if beta2 < 2.9:
            return f"le coefficient de kurtosis de Pearson = {beta2:.4f}\ndonc distribution platykurtique"
        elif 2.9 <= beta2 <= 3.1:
            return f"le coefficient de kurtosis de Pearson = {beta2:.4f}\ndonc distribution mésokurtique"
        else:
            return f"le coefficient de kurtosis de Pearson = {beta2:.4f}\ndonc distribution leptokurtique"


    def __repr__(self):
        return f"la moyenne est: {self.moyenne():.4f}\nla variance est: {self.variance():.4f}\nl'ecart-type est: {self.ecartType():.4f}\n{self.asymetrie()}\n{self.aplatissement()}"


data = [14, 15, 16, 17, 18, 19, 20, 19, 18, 17, 16, 15, 14]

sd = StatDes(data)
print("-------------------------------")
print(sd)
print("-------------------------------")

