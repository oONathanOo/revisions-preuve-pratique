'''On considère la fonction binaire à la page suivante. Cette fonction prend en paramètre
un entier positif a en écriture décimale et renvoie son écriture binaire sous la forme d’une
chaine de caractères.
L’algorithme utilise la méthode des divisions euclidiennes successives comme l’illustre
l’exemple ci-après.

Compléter le code de la fonction binaire.'''
def binaire(a):
    '''convertit un nombre entier a en sa representation
    binaire sous forme de chaine de caractères.'''
    if a == 0:
        return '0'
    bin_a = ''
    while a != 0 :
        bin_a = f'{a%2}' + bin_a
        a = a//2
    return bin_a

'''Exemples :'''
assert binaire(83) == '1010011'
assert binaire(6) == '110'
assert binaire(127) == '1111111'
assert binaire(0) == '0'