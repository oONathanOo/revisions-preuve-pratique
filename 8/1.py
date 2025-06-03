def maximum_tableau(tab):
    max = tab[0]
    for i in range(len(tab)):
        if tab[i] > max:
            max = tab[i]
    return max

assert maximum_tableau([98, 12, 104, 23, 131, 9]) == 131
assert maximum_tableau([-27, 24, -3, 15]) == 24