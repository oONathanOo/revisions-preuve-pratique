
def gb_vers_entier(tab):
    result = 0
    j = 0
    for i in range(len(tab) -1, -1, -1):
        if tab[j] == True:
            result += 2**i
        j += 1
    return result


assert gb_vers_entier([]) == 0
assert gb_vers_entier([True]) == 1
assert gb_vers_entier([True, False, True, False, False, True, True]) == 83
assert gb_vers_entier([True, False, False, False, False, False, True, False]) == 130