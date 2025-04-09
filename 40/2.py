'''Une professeure de NSI décide de gérer les résultats de sa classe sous la forme d’un diction-
naire :

• les clefs sont les noms des élèves ;
• les valeurs sont des dictionnaires dont les clefs sont les types d’épreuves sous forme

de chaîne de caractères et les valeurs sont les notes obtenues associées à leurs coeffi-
cients dans une liste.

Avec :'''
resultats = {
    'Dupont': {
        'DS1': [15.5, 4],
        'DM1': [14.5, 1],
        'DS2': [13, 4],
        'PROJET1': [16, 3],
        'DS3': [14, 4]
    },
    'Durand': {
        'DS1': [6 , 4],
        'DS2': [8, 4],
        'PROJET1': [9, 3],
        'IE1': [7, 2],
        'DS3': [12, 4]
    }
}

'''L’élève dont le nom est Durand a ainsi obtenu au DS2 la note de 8 avec un coefficient 4.
La professeure crée une fonction moyenne qui prend en paramètre le nom d’un de ses
élèves et renvoie sa moyenne arrondie au dixième. Si l’élève n’a pas de notes, on considère
que sa moyenne est nulle. Si le nom donné n’est pas dans les résultats, la fonction renvoie
None.
Compléter le code de la professeure ci-dessous :'''

def moyenne(nom, resultats):
    '''Renvoie la moyenne de l'élève nom, selon le dictionnaire
    resultats. Si nom n'est pas dans le dictionnaire,
    la fonction renvoie None.'''
    if nom in resultats:
        notes = resultats[nom]
        if not notes: # pas de notes
            return 0
        total_points = 0
        total_coefficients = 0
        for valeurs in notes.values():
            note, coefficient = valeurs
            total_points = total_points + note * coefficient
            total_coefficients += coefficient
        return round( total_points / total_coefficients, 1 )
    else:
        return None




'''Exemples :'''
assert moyenne("Dupont", resultats) == 14.5
assert moyenne("Durand", resultats) == 8.5