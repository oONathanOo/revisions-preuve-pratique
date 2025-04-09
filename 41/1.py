def ou_exclusif(tab1, tab2):
    result = []
    for i in range(len(tab1)):
        if tab1[i] == tab2[i] :
            result.append(0)
        else:
            result.append(1)
    return result
   
    
assert ou_exclusif([1, 0, 1, 0, 1, 1, 0, 1], [0, 1, 1, 1, 0, 1, 0, 0]) == [1, 1, 0, 1, 1, 0, 0, 1]
assert ou_exclusif([1, 1, 0, 1], [0, 0, 1, 1]) == [1, 1, 1, 0]