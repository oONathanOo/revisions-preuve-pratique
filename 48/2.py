'''On souhaite programmer une fonction indiquant le point le plus proche d’un point de départ
dans un tableau de points non vide. Les points sont tous à coordonnées entières et sont
donnés sous la forme d’un tuple de deux entiers. Le tableau des points à traiter est donc un
tableau de tuples.
On rappelle que la distance d entre deux points du plan de coordonnées (x; y) et (x′; y′) vérifie la formule : d**2 = (x − x′)**2 + (y − y′)**2

Compléter le code des fonctions distance_carre et point_le_plus_proche
fournies ci-dessous pour qu’elles répondent à leurs spécifications.'''
def distance_carre(point1, point2):
    '''Calcule et renvoie la distance au carre entre
    deux points.'''
    return (point1[0]-point2[0])**2 + (point1[1]-point2[1])**2

def point_le_plus_proche(depart, tab):
    """ Renvoie les coordonnées du premier point du tableau tab se
    trouvant à la plus courte distance du point depart."""
    min_point = tab[0]
    min_dist = distance_carre(tab[0], depart)
    for i in range(1, len(tab)):
        if distance_carre(tab[i], depart) < min_dist:
            min_point = tab[i]
            min_dist = distance_carre(tab[i], depart)
    return min_point

'''Exemples :'''
assert distance_carre((1, 0), (5, 3))==25
assert distance_carre((1, 0), (0, 1))==2
assert point_le_plus_proche((0, 0), [(7, 9), (2, 5), (5, 2)])==(2, 5)
assert point_le_plus_proche((5, 2), [(7, 9), (2, 5), (5, 2)])==(5, 2)