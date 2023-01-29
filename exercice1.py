# pip install numpy  # if numpy module not exist in your system
import numpy as np

def generator(numberOfStudent, minimum, maximum):
    np.random.seed(0)
    return np.random.randint(minimum, maximum, size=numberOfStudent, dtype=int)

def remarque(note):
    if note < 10:
        return 'Non Valide'
    elif note < 12:
        return 'Passable'
    elif note < 14:
        return 'Assez Bien'
    elif note < 16:
        return 'Bien'
    elif note < 18:
        return 'Très Bien'
    else:
        return 'Parfait'

def compterOccurrence(list):
    counts = {}
    for item in list:
        if item[1] not in counts:
            counts[item[1]] = 1
        else:
            counts[item[1]] += 1
    return counts

def valider(notes):
    valide = []
    nonValide = []
    for note in notes:
        if note >= 10:
            valide.append([note,remarque(note)])
        else:
            nonValide.append(note)
    return valide,nonValide



notes = generator(40, 5, 20)
valide, nonValide= valider(notes)
print("--------------------------------")
print(notes)
print("--------------------------------")
print("Valide =" , valide)
print("-----------------")
print(compterOccurrence(valide))
print("--------------------------------")
print("Non Valide = " ,nonValide)
