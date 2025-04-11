'''Un arbre binaire de recherche est soit vide, représenté en Python par la valeur None, soit
un nœud, contenant une étiquette et deux sous-arbres gauche et droit et représenté par
une instance de la classe Noeud donnée ci-dessous.
On considère ici que les étiquettes des nœuds sont des entiers et que les arbres binaires de
recherche considérés ne contiennent pas de doublons.'''
class Noeud:
    def __init__(self, etiquette):
        '''Méthode constructeur pour la classe Noeud.
        Crée une feuille d'étiquette donnée.'''
        self.etiquette = etiquette
        self.gauche = None
        self.droit = None
    
    def inserer(self, cle):
        '''Insère la clé dans l'arbre binaire de recherche
        en préservant sa structure.'''
        if cle < self.etiquette:
            if self.gauche != None:
                self.gauche.inserer(cle)
            else:
                self.gauche = Noeud(cle)
        else:
            if self.droit != None:
                self.droit.inserer(cle)
            else:
                self.droit = Noeud(cle)

'''Compléter la méthode récursive inserer afin qu’elle permette d’insérer une clé dans
l’arbre binaire de recherche non vide sur lequel on l’appelle.
Voici un exemple d’utilisation :'''

arbre = Noeud(7)
for cle in (3, 9, 1, 6):
    arbre.inserer(cle)

assert arbre.gauche.etiquette == 3
assert arbre.droit.etiquette == 9
assert arbre.gauche.gauche.etiquette == 1
assert arbre.gauche.droit.etiquette == 6