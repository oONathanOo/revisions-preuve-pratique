def nb_repetitions(elt, tab):
    n = 0
    for i in tab:
        if i == elt:
            n +=1
    return n
    
    

assert nb_repetitions(5, [2, 5, 3, 5, 6, 9, 5]) == 3
assert nb_repetitions('A', ['B', 'A', 'B', 'A', 'R']) == 2
assert nb_repetitions(12, [1, '!', 7, 21, 36, 44]) == 0