'''La fonction tri_insertion suivante prend en argument un tableau tab (type list) et
trie ce tableau en utilisant la méthode du tri par insertion. Compléter cette fonction pour
qu’elle réponde à la spécification demandée.
On rappelle le principe du tri par insertion : on considère les éléments à trier un par un, le
premier élément constituant, à lui tout seul, un tableau trié de longueur 1. On range ensuite
le second élément pour constituer un tableau trié de longueur 2, puis on range le troisième
élément pour avoir un tableau trié de longueur 3 et ainsi de suite...
A chaque étape, le premier élément du sous-tableau non trié est placé dans le sous-tableau
des éléments déjà triés de sorte que ce sous-tableau demeure trié.
Le principe du tri par insertion est donc d’insérer à la n-ième itération, le n-ième élément à
la bonne place.'''
def tri_insertion(tab):
    '''Trie le tableau tab par ordre croissant
    en appliquant l'algorithme de tri par insertion'''
    n = len(tab)
    for i in range(1, n):
        valeur_insertion = tab[i]
        # la variable j sert à déterminer
        # où placer la valeur à ranger
        j = i
        # tant qu'on n'a pas trouvé la place de l'élément à
        # insérer on décale les valeurs du tableau vers la droite
        print(j, tab[i], valeur_insertion, tab[j])
        while j > 0 and valeur_insertion < tab[j-1]:
            tab[j] = tab[j-1]
            j -= 1
        tab[j] = valeur_insertion
        
'''Exemple :'''
tab = [98, 12, 104, 23, 131, 9]
tri_insertion(tab)
assert tab == [9, 12, 23, 98, 104, 131]