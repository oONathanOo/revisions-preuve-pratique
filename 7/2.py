'''La fonction fusion prend deux tableaux tab1, tab2 (type list) d’entiers triés par ordre
croissant et les fusionne en un tableau trié tab12 qu’elle renvoie.
Compléter le code de la fonction fusion ci-dessous.'''

def fusion(tab1,tab2):
    '''Fusionne deux tableaux triés et renvoie
    le nouveau tableau trié.'''
    n1 = len(tab1)
    n2 = len(tab2)
    tab12 = [0] * (n1 + n2)
    i1 = 0
    i2 = 0
    i = 0
    while i1 < n1 and i2 < n2:
        if tab1[i1] < tab2[i2]:
            tab12[i] = tab1[i1]
            i1 = i1 + 1
        else:
            tab12[i] = tab2[i2]
            i2 = i2 + 1
        i += 1
    while i1 < n1:
        tab12[i] = tab1[i1]
        i1 = i1 + 1
        i = i + 1
    while i2 < n2:
        tab12[i] = tab2[i2]
        i2 = i2 + 1
        i = i + 1
    return tab12


#Exemple :
assert fusion([1,2,3],[]) == [1, 2, 3]
assert fusion([], []) == []
assert fusion([1, 6, 10],[0, 7, 8, 9]) == [0, 1, 6, 7, 8, 9, 10]