#! /usr/bin/python

import sys
"""
Petit jeu d'allumettes
-----------------------
Au départ il y a 30 allumettes, 2 joueurs prennent des à allumettes à tour de rôle.
Celui qui prend la dernière a perdu.
Chaque joueur peut prendre entre 1 et le double du nombre d'allumettes
prises par le précédent.

(c) Marc Augier 2016
    m.augier@me.com

"""

def jeuOrdi(n,m):
    """
    Variables en entrée:
    n est la limite imposée par le tour précédent
    m le nombre d'allumettes restantes

    L'IA du jeu (^_^);
    """
    if m == 1 :
        nb = 1
        print("Bien joué")
    elif n >= (m-1):
        nb = m-1
        print("Je crois que vous êtes mal parti...")
    else :
        laisse = 2 * (n+1)
        nb = max(1,min(n,m - laisse))
    return nb

allumettes = 30
limit = 2

while (allumettes >= 1):
    retire = 0
    while (retire < 1 or retire > min(limit,allumettes)):
        print ("Il y a %i allumettes et vous pouvez en retirer de 1 à %i" % (allumettes, min(limit,allumettes)))
        retire = eval(input("Combien d'allumettes vous voulez retirer ? ==> "))
    allumettes -= retire
    if (allumettes > 0):
        limit = retire*2
        retire = jeuOrdi(limit, allumettes)
        print("A mon tour, je retire %i " % retire)
        allumettes -= retire
        limit = retire*2
        if (allumettes <= 0):
            print("Vous avez gagné !")
    else:
        print("J'ai gagné !")

print("C'est terminé")
