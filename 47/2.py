'''On considère l’algorithme de tri de tableau suivant : à chaque étape, on parcourt le sous-
tableau des éléments non rangés et on place le plus petit élément en première position de

ce sous-tableau.
Exemple avec le tableau :''' 
t = [41, 55, 21, 18, 12, 6, 25]
'''• Étape 1 : on parcourt tous les éléments du tableau, on permute le plus petit élément
avec le premier.
Le tableau devient''' 
t = [6, 55, 21, 18, 12, 41, 25]
'''• Étape 2 : on parcourt tous les éléments sauf le premier, on permute le plus petit
élément trouvé avec le second.
Le tableau devient :''' 
t = [6, 12, 21, 18, 55, 41, 25]
'''Et ainsi de suite.
Le programme ci-dessous implémente cet algorithme.'''

def echange(tab, i, j):
    '''Echange les éléments d'indice i et j dans le tableau tab.'''
    temp = tab[i]
    tab[i] = tab[j]
    tab[j] = temp
    
def tri_selection(tab):
    '''Trie le tableau tab dans l'ordre croissant
    par la méthode du tri par sélection.'''
    N = len(tab)
    for k in range(0, N):
        imin = k
        for i in range(k, N):
            if tab[i] < tab[imin]:
                imin = i
        print(tab)
        echange(tab, k, imin)
        
    return tab

#Compléter ce code de façon à obtenir :
tab = [41, 55, 21, 18, 12, 6, 25]
tri_selection(tab)
print(tab)
assert tab == [6, 12, 18, 21, 25, 41, 55]