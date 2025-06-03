def taille(arbre, lettre):
    while arbre[lettre][0] != '' and arbre[lettre][1] != '':
        return 1 + taille(arbre, arbre[lettre][0]) + taille(arbre, arbre[lettre][1])
    if arbre[lettre][0] == '' and arbre[lettre][1] != '':
        return 1 + taille(arbre, arbre[lettre][1])
    if arbre[lettre][0] != '' and arbre[lettre][1] == '':
        return 1 + taille(arbre, arbre[lettre][0])
    return 1

a = {'F':['B','G'], 'B':['A','D'], 'A':['',''], 'D':['C','E'],'C':['',''], 'E':['',''], 'G':['','I'], 'I':['','H'],'H':['','']}


assert taille(a, 'F') == 9
assert taille(a, 'B') == 5
assert taille(a, 'I') == 2

print(taille(a, 'I'))