def max_et_indice(tab):
    max = tab[0]
    maxindice = 0
    for i in tab[0:]:
        if i > max:
            max = i
            maxindice = tab.index(i)
    return max, maxindice


assert max_et_indice([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]) == (9, 3)
assert max_et_indice([-2]) == (-2, 0)
assert max_et_indice([-1, -1, 3, 3, 3]) == (3, 2)
assert max_et_indice([1, 1, 1, 1]) == (1, 0)