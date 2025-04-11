
def max_dico(dico):
    max_abo = 0
    for nom, abo in dico.items():
        if abo > max_abo:
            max_nom = nom
            max_abo = abo
    return (max_nom, max_abo)


assert max_dico({ 'Bob': 102, 'Ada': 201, 'Alice': 103, 'Tim': 50 }) == ('Ada', 201)
assert max_dico({ 'Alan': 222, 'Ada': 201, 'Eve': 222, 'Tim': 50 }) == ('Alan', 222)