'''On travaille sur des dessins en noir et blanc obtenus à partir de pixels noirs et blancs : La
figure « cœur » ci-dessus va servir d’exemple. On la représente par une grille de nombres,
c’est-à-dire par une liste composée de sous-listes de même longueur. Chaque sous-liste
représentera donc une ligne du dessin.
Dans le code ci-dessous, la fonction affiche permet d’afficher le dessin. Les pixels noirs
(1 dans la grille) seront représentés par le caractère '*' et les pixels blancs (0 dans la grille)
par une espace.
La fonction liste_zoom prend en argument une liste liste_depart et un entier k. Elle
renvoie une liste où chaque élément de liste_depart est dupliqué k fois.
La fonction dessin_zoom prend en argument une grille grille et renvoie une nouvelle
grille où toutes les lignes de grille sont zoomées k fois et répétées k fois.
Compléter les fonctions liste_zoom et dessin_zoom du code suivant :'''

def affiche(dessin):
    ''' affichage d'une grille : les 1 sont représentés par
    un "*" , les 0 par une espace " " '''
    for ligne in dessin:
        affichage = ''
        for col in ligne:
            if col == 1:
                affichage = affichage + "*"
            else:
                affichage = affichage + " "
        print(affichage)
        
def liste_zoom(liste_depart,k):
    '''renvoie une liste contenant k fois chaque élément de
    liste_depart'''
    liste_zoomee = []
    for elt in liste_depart:
        for i in range(k):
            liste_zoomee.append(elt)
    return liste_zoomee

def dessin_zoom(grille,k):
    '''renvoie une grille où les lignes sont zoomées k fois
    ET répétées k fois'''
    grille_zoomee=[]
    for ligne in grille:
        ligne_zoomee = liste_zoom(ligne, k)
        for i in range(k):
            grille_zoomee.append(ligne_zoomee)
    return grille_zoomee

'''Exemples :'''
coeur = [[0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
[0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
[0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
[0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]]

affiche(dessin_zoom(coeur,2))
assert liste_zoom([1,2,3],3) == [1, 1, 1, 2, 2, 2, 3, 3, 3]