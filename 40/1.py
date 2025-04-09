
def recherche_indices_classement(elt, tab):
    r1 = []
    r2 = []
    r3 = []
    idx = enumerate(tab)
    for i in idx:
        if i[1] < elt:
            r1.append(i[0])
        if i[1] == elt:
            r2.append(i[0])
        if i[1] > elt:
            r3.append(i[0])
    return (r1, r2, r3)

assert recherche_indices_classement(3, [1, 3, 4, 2, 4, 6, 3, 0]) == ([0, 3, 7], [1, 6], [2, 4, 5])
assert recherche_indices_classement(3, [1, 4, 2, 4, 6, 0]) == ([0, 2, 5], [], [1, 3, 4])
assert recherche_indices_classement(3, [1, 1, 1, 1]) == ([0, 1, 2, 3], [], [])
assert recherche_indices_classement(3, []) == ([], [], [])