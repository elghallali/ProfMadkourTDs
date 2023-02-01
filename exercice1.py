# pip install numpy  # if numpy module not exist in your system
import numpy as np

def generator(numberOfStudent, minimum= 0, maximum=20):
    np.random.seed(0)
    return np.random.randint(minimum, maximum, size=numberOfStudent, dtype=int)

def valider(notes):
    valide = []
    nonValide = []
    for note in notes:
        if note >= 10:
            valide.append((note))
        else:
            nonValide.append(note)
    return valide,nonValide



notes = generator(40)
valide, nonValide= valider(notes)
print("--------------------------------")
print(notes)
print("--------------------------------")
print("Valide =" , valide)
print("--------------------------------")
print("Non Valide = " ,nonValide)
