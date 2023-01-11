# Prof MADKOUR TDs

## Des structures de contrôle et des structures de données en interaction

### Exercice 1:

1. Générer 100 nombres aléatoires compris entre 0 et 20 (notes d'étudiants dans un module)
2. Etablir la liste des notes supérieures ou égales à 10 (notes des étudiants ayant validé le mdule) et la liste des notes strictement inférieures à 10 (notes des étudiants n'ayant pas validé le module)
#### **Etape 1:** Générer des nombres aléatoires:

1. On importe le module numpy: import numpy as np

2. On fixe la valeur de la graine (à 0 par exemple): np.random.seed(0)

3. Utiliser la fonction randint pour générer des nombres aléatoires [cliquer ici pour accéder à la documentation](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html#numpy-random-randint){:target="_blank"}

#### **Etape 2 :** Créer 2 listes vides:

+ valide pour collecter les notes des étudiants ayant validé le module.

+ non_valide pour collecter les notes des étudiants n'ayant pas validé le module.

#### **Etape 3 :** A l'aide de boucle for, de test condtionnel if / elif / else et des méthodes des listes:

+ Affecter les notes qui sont supérieures ou égales à 10 à la liste valide.

+ Affecter les notes qui sont strictement inférieures à 10 à la liste non_valide.
