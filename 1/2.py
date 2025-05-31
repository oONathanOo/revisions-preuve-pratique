'''On considère dans cet exercice la suite de nombre suivante : 1, 11, 21, 1211, 111221, ...
Cette suite est construite ainsi : pour passer d’une valeur à la suivante, on la lit et on l’écrit
sous la forme d’un nombre. Ainsi, pour 1211 :
• on lit un 1, un 2, deux 1 ;
• on écrit donc en nombre 1 1, 1 2, 2 1 ;
• puis on concatène 111221.
Compléter la fonction nombre_suivant qui prend en entrée un nombre sous forme de
chaine de caractère et qui renvoie le nombre suivant par ce procédé, encore sous forme de
chaîne de caractère.'''

def nombre_suivant(s):
    '''Renvoie le nombre suivant de celui representé par s
    en appliquant le procédé de lecture.'''
    resultat = ''
    chiffre = s[0]
    compte = 1
    for i in range(1, len(s)):
        if s[i] == chiffre:
            compte = 2
        else:
            resultat += str(compte) + chiffre
            chiffre = s[i]
            compte = 1
    lecture_chiffre = str(compte) + chiffre
    resultat += lecture_chiffre
    return resultat

assert nombre_suivant('1211') == '111221'
assert nombre_suivant('311') == '1321'