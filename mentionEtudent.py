def resultats(number):
    import numpy as np
    np.random.seed(0)

    notes = list(np.random.randint(low=0,high=20,size=number, dtype=int))

    students = [f'student_{i+1}' for i in range(number)]

    favorable = {student : note for student, note in zip(students, notes) if note >= 10}
    unfavorable = {student : note for student, note in zip(students, notes) if note < 10}

    mentions = {}

    for student in favorable.keys():
        if 10 <= favorable[student] < 12:
            mentions[student] = 'Passable'
        elif 12 <= favorable[student] < 14:
            mentions[student] = 'Assez Bien'
        elif 14 <= favorable[student] < 16:
            mentions[student] = 'Bien'
        elif 16 <= favorable[student] < 18:
            mentions[student] = 'Très Bien'
        elif favorable[student] >= 18:
            mentions[student] = 'Excellent'
    return mentions
les_mentions = resultats(40)

print(f'La liste des mentions des étudiants : {les_mentions}')