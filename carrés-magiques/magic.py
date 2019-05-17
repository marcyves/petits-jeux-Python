#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
"""
    Carrés magiques
    ===============

    Ce programme génère des carrés magiques de taille quelconque mais impaire
    en utilisant la méthode diagonale décrite à la page :
    http://villemin.gerard.free.fr/Wwwgvmm/CarreMag/aaaMaths/Diagonal.htm

    Un carré magique est un carré de nombres dans lequel les sommes des
    nombres de chaque rangée, de chaque colonne et des deux diagonales sont
    égales.

    L'ordinateur demande la taille, seuls les nombres impairs sont acceptés.
   
"""

def choix_taille():

    taille  = 0
    print("Choisissez la taille du carré")
    while (taille%2 == 0):
        taille = int(input("Entrez un nombre impair ==>  "))
    
    return taille

class magic:
    def __init__(self, taille):
        self.taille = taille
        self.tableau = [0 for x in range(taille**2)]

    def __str__(self):
        row_format ="{:>5} | "
        tmp = ""
        for ligne in range(1, self.taille+1):
            valeur = 0
            for colonne in range(1, self.taille+1):
                valeur += self.getTableau(ligne, colonne)
                tmp += row_format.format(self.getTableau(ligne, colonne))
            tmp += " = {}\n".format(valeur)

        t=0
        for i in range(1, self.taille+1):
            t = t + self.getTableau(i, 1)

        tmp += "Tableau de force {}".format(t)

        return tmp

    def setTableau(self, ligne, colonne, valeur):
        position = (ligne-1)*self.taille + colonne -1
        # print( " ({},{}) = {} - position {}".format(ligne, colonne, valeur, position))
        if self.tableau[position] == 0:
            self.tableau[position] = valeur

    def getTableau(self, ligne, colonne):
        position = (ligne-1)*self.taille + colonne -1
        # print("get ({},{}) = {}".format(ligne, colonne, position))
        return self.tableau[position]

    def calcule_carre(self):
        for i in range(1, self.taille+1):
            for j in range(1, self.taille+1):
                q = (i + j + (self.taille-1)/2 - 1)%self.taille
                r = (i + 2*j -2)%self.taille
                self.setTableau(i, j, self.taille*q+r+1)


print("="*30)
print("\tCarrés magiques conventionnel avec les nombres de 1 à n²")
print("="*30)

taille = choix_taille()
mon_carre =  magic(taille)
mon_carre.calcule_carre()
print(mon_carre)