import numpy as np


class StatDes:
    def __init__(self, dataSet):
        self.dataSet = dataSet

    def moyenne(self):
        sum = 0
        for i in self.dataSet:
            sum += i
        return sum / len(self.dataSet)

    def variance(self):
        sum = 0
        for i in self.dataSet:
            sum += i**2
        sum /= len(self.dataSet)
        return sum - self.moyenne()**2

    def ecartType(self):
        return np.sqrt(self.variance())

    def asymetrie(self):
        sum = 0
        for i in self.dataSet:
            sum += ((i - self.moyenne()) / self.ecartType())**3
        sum /= len(self.dataSet)
        if sum < -0.2:
            return f"le coefficient de Skewness = {sum:.4f}\ndonc la distribution est asymétrique à gauche"
        elif -0.2 <= sum <= 0.2:
            return f"le coefficient de Skewness = {sum:.4f}\ndonc la distribution est symétrique"
        else:
            return f"le coefficient de Skewness = {sum:.4f}\ndonc la distribution est asymétrique à droite"

    def aplatissement(self):
        sum = 0
        for i in self.dataSet:
            sum += ((i - self.moyenne()) / self.ecartType())**4
        sum /= len(self.dataSet)
        if sum < 2.9:
            return f"le coefficient de kurtosis de Pearson = {sum:.4f}\ndonc distribution platykurtique"
        elif -0.9 <= sum <= 3.1:
            return f"le coefficient de kurtosis de Pearson = {sum:.4f}\ndonc distribution mésokurtique"
        else:
            return f"le coefficient de kurtosis de Pearson = {sum:.4f}\ndonc distribution leptokurtique"


    def __repr__(self):
        return f"la moyenne est: {self.moyenne():.4f}\nla variance est: {self.variance():.4f}\nl'ecart-type est: {self.ecartType():.4f}\n{self.asymetrie()}\n{self.aplatissement()}"


data = [14, 15, 16, 17, 18, 19, 20, 19, 18, 17, 16, 15, 14]

sd = StatDes(data)
print("-------------------------------")
print(sd)
print("-------------------------------")

