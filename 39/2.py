'''On considère un tableau d’entiers tab (de type list) dont les éléments sont des 0 ou des
1). On se propose de trier ce tableau selon l’algorithme suivant : à chaque étape du tri, le
tableau est constitué de trois zones consécutives, la première ne contenant que des 0, la
seconde n’étant pas triée et la dernière ne contenant que des 1. Au départ, les zones ne
contenant que des 0 et des 1 sont vides.
[0, ..., 0, <zone non triée>, 1, ..., 1]
Tant que la zone non triée n’est pas réduite à un seul élément, on regarde son premier
élément :
• si cet élément vaut 0, on considère qu’il appartient désormais à la zone ne contenant
que des 0 ;
• si cet élément vaut 1, il est échangé avec le dernier élément de la zone non triée et on
considère alors qu’il appartient à la zone ne contenant que des 1.
Dans tous les cas, la longueur de la zone non triée diminue de 1.
Compléter la fonction tri suivante :'''

def tri(tab):
    '''tab est un tableau d'entiers contenant des 0 et des 1.
    La fonction trie ce tableau en plaçant tous les 0 à gauche'''
    i = 0 # premier indice de la zone non triée
    j = len(tab)-1 # dernier indice de la zone non triée
    while i < j:
        if tab[i] == 0:
            i += 1
        else:
            valeur = tab[j]
            tab[j] = tab[i]
            tab[i] = valeur
            j -= 1

'''Exemple :'''
tab = [0,1,0,1,0,1,0,1,0]
tri(tab)
assert tab == [0, 0, 0, 0, 0, 1, 1, 1, 1]