
def nombre_de_mots(phrase):
    mots = 0
    for i in phrase:
        if i == ' ' or i == '.':
            mots += 1
    return mots

assert nombre_de_mots('Cet exercice est simple.') == 4
assert nombre_de_mots('Le point d exclamation est séparé !') == 6
assert nombre_de_mots('Combien de mots y a t il dans cette phrase ?') == 10
assert nombre_de_mots('Fin.') == 1