class Noeud:
    def __init__(self, etiquette, gauche, droit):
        self.v = etiquette
        self.gauche = gauche
        self.droit = droit

def taille(a):
    if a == None:
        return 0
    return 1 + taille(a.gauche) + taille(a.droit)

def hauteur(a):
    if a == None:
        return -1
    return max(taille(a.gauche), taille(a.droit))
        

a = Noeud(1, Noeud(4, None, None), Noeud(0, None, Noeud(7, None, None)))

print(taille(a))