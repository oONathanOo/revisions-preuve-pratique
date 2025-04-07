def recherche(tab = list, n = int):
    if n not in tab:
        return None
    for i in range(len(tab)-1, -1, -1):
        if tab[i] == n:
            return i


print(recherche([2, 0, 2],2))

assert recherche([5, 3],1) == None
assert recherche([2,4],2) == 0
assert recherche([2,3,5,2,4],2) == 3