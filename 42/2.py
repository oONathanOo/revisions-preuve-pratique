'''Pour rappel, la conversion d’un nombre entier positif en binaire peut s’effectuer à l’aide des
divisions successives comme illustré ici :

Voici une fonction Python basée sur la méthode des divisions successives permettant de
convertir un nombre entier positif en binaire :
Compléter la fonction binaire.'''
def binaire(a):
    '''convertit un nombre entier a en sa representation
    binaire sous forme de chaine de caractères.'''
    if a == 0:
        return '0'
    bin_a = ''
    while a != 0:
        bin_a = f'{a%2}' + bin_a
        a = a//2
    return bin_a

'''Exemples :'''
assert binaire(0) == '0'
assert binaire(77) == '1001101'