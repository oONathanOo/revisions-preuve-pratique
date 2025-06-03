'''On considère un tableau non vide de nombre entiers, positifs ou négatifs, et on souhaite
déterminer la plus grande somme possible de ses éléments consécutifs.
Par exemple, dans le tableau [1, -2, 3, 10, -4, 7, 2, -5], la plus grande
somme est 18 obtenue en additionnant les éléments 3, 10, -4, 7, 2.
Pour cela, on va résoudre le problème par programmation dynamique. Si on note tab le
tableau considéré et i un indice dans ce tableau, on se ramène à un problème plus simple
: déterminer la plus grande somme possible de ses éléments consécutifs se terminant à
l’indice i.
Si on connait la plus grande somme possible de ses éléments consécutifs se terminant à
l’indice i-1, on peut déterminer la plus grande somme possible de ses éléments consécutifs
se terminant à l’indice i :

• soit on obtient une plus grande somme en ajoutant tab[i] à cette somme précé-
dente ;

• soit on commence une nouvelle somme à partir de tab[i].
Compléter la fonction somme_max ci-dessous qui réalise cet algorithme.'''

def somme_max(tab):
    n = len(tab)
    sommes_max = [0]*n
    sommes_max[0] = tab[0]
    # on calcule la plus grande somme se terminant en i
    for i in range(1,n):
        if tab[i] + sommes_max[i-1] > tab[i]:
            sommes_max[i] = sommes_max[i-1] + tab[i]
        else:
            sommes_max[i] = tab[i]
# on en déduit la plus grande somme de celles-ci
    maximum = 0
    for i in range(1, n):
        if sommes_max[i] > sommes_max[maximum]:
            maximum = i
    return sommes_max[maximum]

#Exemples :

print(somme_max([1, -2, 3, 10, -4, 7, 2, -5]))

assert somme_max([1, 2, 3, 4, 5]) == 15
assert somme_max([1, 2, -3, 4, 5]) == 9
assert somme_max([1, 2, -2, 4, 5]) == 10
assert somme_max([1, -2, 3, 10, -4, 7, 2, -5]) == 18


# Cas avec tous les nombres négatifs : le plus grand sous-ensemble est le plus grand nombre seul
assert somme_max([-8, -3, -6, -2, -5, -4]) == -2

# Cas avec une seule valeur positive au milieu
assert somme_max([-2, -3, 5, -1, -2]) == 5

# Cas avec des zéros (ne changent pas la somme, mais coupent parfois les sous-ensembles)
assert somme_max([0, -3, 5, 0, -2, 0, 4]) == 7

# Cas avec tous les nombres positifs (la somme de toute la liste)
assert somme_max([10, 20, 30]) == 60

# Cas où la sous-séquence maximale est à la fin
assert somme_max([-4, -1, 2, 1, 5]) == 8