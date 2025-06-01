def ecriture_binaire_entier_positif(n):
    result = ''
    if n == 0:
        return '0'
    while n != 0:
        result = str(n%2) + result
        n = n//2
    return result

assert ecriture_binaire_entier_positif(0) == '0'
assert ecriture_binaire_entier_positif(2) == '10'
assert ecriture_binaire_entier_positif(105) == '1101001'