def delta(tab):
    if len(tab) == 1:
        return tab
    result = [tab[0]]
    for i in range(1, len(tab)):
        result.append(tab[i]-tab[i-1])
    return result

assert delta([1000, 800, 802, 1000, 1003]) == [1000, -200, 2, 198, 3]
assert delta([42]) == [42]