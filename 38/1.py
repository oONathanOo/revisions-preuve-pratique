def moyenne(tab):
    num = 0
    den = len(tab)
    if den != 0:
        for i in tab:
            num += i
    return num/den

assert moyenne([1.0]) == 1.0
assert moyenne([1.0, 2.0, 4.0]) == 2.3333333333333335