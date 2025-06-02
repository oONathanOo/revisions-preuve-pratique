def liste_puissances(a, n):
    result = []
    val = a
    for i in range(1, n+1):
        result.append((val))
        val = val * a
    return result


def liste_puissances_borne(a, borne):
    result = []
    for i in liste_puissances(a, borne):
        if i < borne:
            result.append(i)
    return result


assert liste_puissances(3, 5) == [3, 9, 27, 81, 243]
assert liste_puissances(-2, 4) == [-2, 4, -8, 16]
assert liste_puissances_borne(2, 16) == [2, 4, 8]
assert liste_puissances_borne(2, 17) == [2, 4, 8, 16]
assert liste_puissances_borne(5, 5) == []