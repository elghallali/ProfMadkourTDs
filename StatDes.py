import math


class StatDes:
    # Constructor Method
    def __init__(self, dataSet):
        self.dataSet = dataSet
        self.__len = len(dataSet)

    # Mean Method
    def moyenne(self):
        return sum(self.dataSet) / self.__len

    # Variance Method
    def variance(self):
        v = [i**2 for i in self.dataSet]
        return sum(v)/self.__len - self.moyenne()**2

    # Standard Deviation Method
    def ecartType(self):
        return math.sqrt(self.variance())

    # Skewness Method
    def asymetrie(self):
        asy = [((i - self.moyenne()) / self.ecartType())**3 for i in self.dataSet]
        gamma1 = sum(asy) / self.__len
        if gamma1 < -0.2:
            return f"le coefficient de Skewness = {gamma1:.4f}\ndonc la distribution est asymétrique à gauche"
        elif gamma1 <= 0.2:
            return f"le coefficient de Skewness = {gamma1:.4f}\ndonc la distribution est symétrique"
        else:
            return f"le coefficient de Skewness = {gamma1:.4f}\ndonc la distribution est asymétrique à droite"

    # Kurtosis Method
    def aplatissement(self):
        ap =[ ((i - self.moyenne()) / self.ecartType())**4 for i in self.dataSet]
        beta2 = sum(ap) / self.__len
        if beta2 < 2.9:
            return f"le coefficient de kurtosis de Pearson = {beta2:.4f}\ndonc distribution platykurtique"
        elif beta2 <= 3.1:
            return f"le coefficient de kurtosis de Pearson = {beta2:.4f}\ndonc distribution mésokurtique"
        else:
            return f"le coefficient de kurtosis de Pearson = {beta2:.4f}\ndonc distribution leptokurtique"

    # Affichage Method (Magic Method)
    def __repr__(self):
        return f"la moyenne est: {self.moyenne():.4f}\nla variance est: {self.variance():.4f}\nl'ecart-type est: {self.ecartType():.4f}\n{self.asymetrie()}\n{self.aplatissement()}"


data = [14, 15, 16, 17, 18, 19, 20, 19, 18, 17, 16, 15, 14]

sd = StatDes(data)
print("-------------------------------")
print(sd)
print("-------------------------------")

