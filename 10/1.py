def recherche(tab, n):
    for i in range(len(tab)-1):
        if tab[i] == n:
            return i
    return None

assert recherche([2, 3, 4, 5, 6], 5) == 3
assert recherche([2, 3, 4, 6, 7], 5) == None