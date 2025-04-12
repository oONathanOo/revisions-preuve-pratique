def recherche_motif(motif, chaine):
    result = []
    for i in range(len(chaine) - 1):
        if chaine[i] + chaine[i+1] == motif:
            result.append(i)
    return result


assert recherche_motif("ab", "") == []
assert recherche_motif("ab", "cdcdcdcd") == []
assert recherche_motif("ab", "abracadabra") == [0, 7]
assert recherche_motif("ab", "abracadabraab") == [0, 7, 11]