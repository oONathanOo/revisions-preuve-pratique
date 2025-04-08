'''Soit une image binaire représentée dans un tableau à 2 dimensions. Les éléments M[i][j],
appelés pixels, sont égaux soit à 0 soit à 1.
Une composante d’une image est un sous-ensemble de l’image constitué uniquement de 1
et de 0 qui sont côte à côte, soit horizontalement soit verticalement.

On souhaite, à partir d’un pixel égal à 1 dans une image M, donner la valeur val à tous les
pixels de la composante à laquelle appartient ce pixel.
La fonction colore_comp1 prend pour paramètre une image M (représentée par une liste
de listes), deux entiers i et j et une valeur entière val. Elle met à la valeur val tous les
pixels de la composante du pixel M[i][j] s’il vaut 1 et ne fait rien sinon.

Par exemple, colore_comp1(M, 2, 1, 3) donne
Compléter le code récursif de la fonction colore_comp1 donné ci-dessous :'''

def colore_comp1(M, i, j, val):
    if M[i][j] != 1:
        return
    M[i][j] = val
    if i-1 >= 0: # propage en haut
        colore_comp1(M, i-1, j, val)
    if i+1 < len(M): # propage en bas
        colore_comp1(M, i+1, j, val)
    if j-1 >= 0: # propage à gauche
        colore_comp1(M, i, j-1, val)
    if j+1 <= len(M[i]): # propage à droite
        colore_comp1(M, i, j+1, val)

'''Exemple :'''

M = [[0, 0, 1, 0], [0, 1, 0, 1], [1, 1, 1, 0], [0, 1, 1, 0]]
colore_comp1(M, 2, 1, 3)
assert M == [[0, 0, 1, 0], [0, 3, 0, 1], [3, 3, 3, 0], [0, 3, 3, 0]]