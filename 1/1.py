
adj = [[1, 2], [2], [0], [0]]

def voisins_entrants(adj, x):
    result = []
    for i in enumerate(adj):
        if x in i[1]:
            result.append(i[0])
    return result


assert voisins_entrants(adj, 0) == [2, 3]
assert voisins_entrants(adj, 1) == [0]