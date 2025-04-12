'''On s’intéresse à un algorithme récursif qui permet de rendre la monnaie à partir d’une liste
donnée de valeurs de pièces et de billets.
Le système monétaire est donné sous forme d’une liste valeurs = [100, 50, 20,
10, 5, 2, 1]. On suppose que les pièces et les billets sont disponibles sans limitation.
On cherche à donner la liste des valeurs à rendre pour une somme donnée en argument.
L’algorithme utilisé est de type glouton.
Compléter le code Python ci-dessous de la fonction rendu_glouton qui implémente cet
algorithme et renvoie la liste des pièces à rendre.'''
valeurs = [100, 50, 20, 10, 5, 2, 1]
def rendu_glouton(a_rendre, rang):
    if a_rendre == 0:
        return []
    v = valeurs[rang]
    if v <= a_rendre:
        return [v] + rendu_glouton(a_rendre - v, rang)
    else:
        return rendu_glouton(a_rendre, rang+1)

'''On devra obtenir :'''

assert rendu_glouton(67, 0) == [50, 10, 5, 2]
assert rendu_glouton(291, 0) == [100, 100, 50, 20, 20, 1]
assert rendu_glouton(291,1) == [50, 50, 50, 50, 50, 20, 20, 1]