def nbr_occurrences(chaine):
    result = {}
    for i in chaine:
        result[i] = 0
    for j in chaine:
        if j in result:
            result[j] += 1
    return result

print(nbr_occurrences('Hello World !'))