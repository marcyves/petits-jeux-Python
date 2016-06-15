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

allumettes = 30


while (allumettes > 1):
    print("Il y a %i allumettes"% allumettes)
    retire = eval(input("Combien d'allumettes vous voulez retirer ?"))
    allumettes -= retire

print("C'est terminé")
