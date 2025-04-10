
def moyenne(tab):
    num = 0
    den = len(tab)
    for i in tab:
        num += i 
    if den == 0:
        return None
    return num/den



assert moyenne([5,3,8]) == 5.333333333333333
assert moyenne([1,2,3,4,5,6,7,8,9,10]) == 5.5
assert moyenne([]) == None