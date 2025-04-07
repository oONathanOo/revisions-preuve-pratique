def compte_occurrences(x, list):
    result = 0
    for i in list:
        if x == i:
            result += 1
    return result

assert compte_occurrences(5, []) == 0
assert compte_occurrences(5, [-2, 3, 1, 5, 3, 7, 4]) == 1
assert compte_occurrences('a', ['a','b','c','a','d','e','a']) == 3