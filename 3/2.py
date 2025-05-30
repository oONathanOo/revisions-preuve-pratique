'''On considère la fonction eleves_du_mois prenant en paramètres eleves et notes
deux tableaux non vides de même longueur, le premier contenant le nom des élèves et le
second, des entiers positifs désignant leur note à un contrôle de sorte que eleves[i] a
obtenu la note notes[i].
Cette fonction renvoie le couple constitué de la note maximale attribuée et des noms des
élèves ayant obtenu cette note regroupés dans un tableau.
Ainsi, l’instruction eleves_du_mois(['a', 'b', 'c', 'd'], [15, 18, 12,
18]) renvoie le couple (18, ['b', 'd']).
Compléter le code suivant :'''

def eleves_du_mois(eleves, notes):
    note_maxi = 0
    meilleurs_eleves = []
    for i in range(len(notes)):
        if notes[i] == note_maxi:
            meilleurs_eleves.append(eleves[i])
        elif notes[i] > note_maxi:
            note_maxi = notes[i]
            meilleurs_eleves = [eleves[i]]
    return (note_maxi, meilleurs_eleves)

#Exemples :
eleves_nsi = ['a','b','c','d','e','f','g','h','i','j']
notes_nsi = [30, 40, 80, 60, 58, 80, 75, 80, 60, 24]
assert eleves_du_mois(eleves_nsi, notes_nsi) == (80, ['c', 'f', 'h'])