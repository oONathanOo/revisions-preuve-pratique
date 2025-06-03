
def parcours_largeur(arbre):
    if arbre is None:
        return []
    file = [arbre]
    resultat = []
    while file:
        noeud = file.pop(0)
        if noeud is not None:
            resultat.append(noeud[1])
            file.append(noeud[0])
            file.append(noeud[2])
    return resultat
        



arbre = ( ( (None, 1, None), 2, (None, 3, None) ), 4, ( (None, 5, None), 6, (None, 7, None) ) )

print(parcours_largeur(arbre))

#assert parcours_largeur(arbre) == [4, 2, 6, 1, 3, 5, 7]