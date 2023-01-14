# pip install numpy  # if numpy module not exist in your system
import numpy as np

def generator(number):
    np.random.seed(0)
    return np.random.randint(0, 20, size=number)

def valider(list):
    valide = []
    nonValide = []
    for i in list:
        if i >= 10:
            valide.append(i)
        else:
            nonValide.append(i)
    return valide,nonValide



z = generator(100)
valide, nonValide= valide(z)

print(z)
print(valide)
print(nonValide)
