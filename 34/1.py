
def tri_selection(tab):
    for j in range(len(tab)-1):
        min = j
        for i in range(j+1, len(tab)):
            if tab[i] < tab[min]:
                min = i
        tab[j], tab[min] = tab[min], tab[j]
    return tab

tab = [1, 52, 6, -9, 12]
tri_selection(tab)
print(tab)
assert tab == [-9, 1, 6, 12, 52]