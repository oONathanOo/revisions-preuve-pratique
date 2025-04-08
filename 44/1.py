def moyenne(list):
    result = []
    denominator = []
    for i in list:
        for j in i:
            result.append(i[0]*(i[1]))
            denominator.append(i[1])
    if sum(denominator) > 0:
        return sum(result)/sum(denominator)
    else:
        return None

assert moyenne([(8, 2), (12, 0), (13.5, 1), (5, 0.5)]) == 9.142857142857142
assert moyenne([(3, 0), (5, 0)]) == None