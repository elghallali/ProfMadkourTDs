# pip install numpy  # if numpy module not exist in your system
import numpy as np

def generator(number):
    np.random.seed(0)
    return np.random.randint(0, 20, size=number, dtype=int)

def valider(notes):
    valide = []
    nonValide = []
    for note in notes:
        if note >= 10:
            valide.append(note)
        else:
            nonValide.append(note)
    return valide,nonValide



notes = generator(100)
valide, nonValide= valider(notes)
print("--------------------------------")
print(notes)
print("--------------------------------")
print("Nalide =" , valide)
print("--------------------------------")
print("Non Valide = " ,nonValide)
