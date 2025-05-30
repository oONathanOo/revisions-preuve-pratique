'''Le jeu du « plus ou moins » consiste à deviner un nombre entier choisi entre 1 et 99.
Une élève de NSI décide de le coder en langage Python de la manière suivante :
• le programme génère un nombre entier aléatoire compris entre 1 et 99 ;
• si la proposition de l’utilisatrice est plus petite que le nombre cherché, l’utilisatrice en
est avertie. Elle peut alors en tester un autre ;
• si la proposition de l’utilisatrice est plus grande que le nombre cherché, l’utilisatrice
en est avertie. Elle peut alors en tester un autre ;
• si l’utilisatrice trouve le bon nombre en 10 essais ou moins, elle gagne ;
• si l’utilisatrice a fait plus de 10 essais sans trouver le bon nombre, elle perd.
La fonction randint est utilisée.
Si a et b sont des entiers tels que a <= b, randint(a,b) renvoie un nombre entier
compris entre a et b inclus.
Compléter le code ci-dessous et le tester :'''
from random import randint
def plus_ou_moins():
    nb_mystere = randint(1, 99)
    nb_test = int(input("Proposez un nombre entre 1 et 99 : "))
    compteur = 0
    while nb_mystere != nb_test and compteur < 10:
        compteur = compteur + 1
        if nb_mystere > nb_test:
            nb_test = int(input("Trop petit ! Testez encore : "))
        else:
            nb_test = int(input("Trop grand ! Testez encore : "))

    if nb_mystere == nb_test:
        print ("Bravo ! Le nombre était ", nb_mystere)
        print("Nombre d'essais: ", compteur)
    else:
        print ("Perdu ! Le nombre était ", nb_mystere)

plus_ou_moins()