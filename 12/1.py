def fusion(tab1, tab2):
    temp = tab1 + tab2
    result = []
    for _ in range(len(temp)):
        result.append(min(temp))
        temp.pop(temp.index(min(temp)))
    return result


print(fusion([3, 5], [2, 5]))