
def insertion_abr(a, cle):
    if a == None:
        return (None, cle, None)
    g, v, d = a
    if cle == v:
        return a
    else:
        if cle < v:
            return (insertion_abr(g, cle), v, d)
        else:
            return (g, v, insertion_abr(d, cle))


n0 = (None, 0, None)
n3 = (None, 3, None)
n2 = (None, 2, n3)
abr1 = (n0, 1, n2)

assert insertion_abr(abr1, 4) == ((None,0,None),1,(None,2,(None,3,(None,4,None))))
assert insertion_abr(abr1, -5) == (((None,-5,None),0,None),1,(None,2,(None,3,None)))
assert insertion_abr(abr1, 2) == ((None,0,None),1,(None,2,(None,3,None)))