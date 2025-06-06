'''Un nombre premier est un nombre entier naturel qui admet exactement deux diviseurs
distincts entiers et positifs : 1 et lui-même.
Le crible d’Ératosthène permet de déterminer les nombres premiers plus petit qu’un certain
nombre n fixé strictement supérieur à 1.
On considère pour cela un tableau tab de n booléens (type list), initialement tous égaux

à True, sauf tab[0] et tab[1] qui valent False, 0 et 1 n’étant pas des nombres pre-
miers.

On parcourt alors ce tableau de gauche à droite et pour chaque indice i :
• si tab[i] vaut True : le nombre i est premier et on donne la valeur False à toutes
les cases du tableau dont l’indice est un multiple de i, à partir de 2*i (c’est-à-dire
2*i, 3*i ...).

• si tab[i] vaut False : le nombre i n’est pas premier et on n’effectue aucun change-
ment sur le tableau.

On dispose de la fonction crible, donnée ci-dessous et à compléter, prenant en paramètre
un entier n strictement supérieur à 1 et renvoyant un tableau contenant tous les nombres
premiers plus petits que n.'''

def crible(n):
    """Renvoie un tableau contenant tous les nombres premiers
    plus petits que n."""
    premiers = []
    tab = [True] * n
    tab[0], tab[1] = False, False
    for i in range(n):
        if tab[i]:
            premiers.append(i)
            multiple = 2*i
            while multiple < n:
                tab[multiple] = False
                multiple = multiple + i
    return premiers

#Exemples :

assert crible(40) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
assert crible(5) == [2, 3]