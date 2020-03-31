#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
    Carrés Magiques
    ===============

    Ce script génère des carrés magiques.

"""

class carreMagique:

    def __init__(self, taille):
        self.taille = taille
        self.tableau = [[0 for x in range(taille)] for x in range(taille)]

    def calcule_carre(self):
        pass

    def affiche_carre(self):
        for ligne in range(1, self.taille + 1):
            for col in range(1, self.taille +1):
                print(self.getXY(ligne, col), end=" ")
            print("")

    def getXY(self, x, y):
        x = x - 1
        y = y - 1
        return self.tableau[x][y]

    def setXY(self, x , y, valeur):
        x = x - 1
        y = y - 1
        self.tableau[x][y] = valeur

def choix_taille():
    return 5

# Le programme commence ici
if __name__ == "__main__":
    print("Carrés magiques")

    taille = choix_taille()

    mon_carre = carreMagique(taille)

    mon_carre.calcule_carre()
    mon_carre.affiche_carre()