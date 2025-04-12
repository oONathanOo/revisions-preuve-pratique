def occurrences(car, chaine):
    result = 0
    for i in chaine:
        if i == car:
            result += 1
    return result


assert occurrences('e', "sciences") == 2
assert occurrences('i',"mississippi") == 4
assert occurrences('a',"mississippi") == 0