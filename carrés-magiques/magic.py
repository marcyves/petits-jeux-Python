#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
"""
    Carrés magiques
    ===============

    Ce programme généère des carrés magiques de quatre tailles différentes 
    en utilisant la méthode dite "de La Loubère".

    Un carré magique est un carré de nombres dans lequel les sommes des
    nombres de chaque rangée, de chaque colonne et des deux diagonales sont
    égales.

    L'ordinateur demande la taille de 1 à 9.
    Seuls les nombres impairs sont acceptés.

    Méthode dite de la Loubère :
    ============================
    Placer 1 à droite de la ligne médiane, les autres nombres qui suivent sont écrits :
     si la case est libre, en bas à droite de leur prédécesseur
     sinon directement à gauche de la case occupée.
    
    En cas de dépassement de ligne ou de colonne, aller à l'autre extrémité.

"""

def choix_taille():

    taille  = 0
    print("Choisissez la taille du carré")
    while (taille <= 0 or taille > 9 or taille%2 == 0):
        taille = int(input("Entrez un nombre impair entre 1 et 9 ==>  "))
    
    return taille

class magic:
    def __init__(self, taille):
        self.taille = taille
        self.tableau = [0 for x in range(taille**2)]

    def __str__(self):
        tmp = ""
        for ligne in range(1, self.taille+1):
            for colonne in range(1, self.taille+1):
                tmp += str(self.getTableau(ligne, colonne))
            tmp += "\n"
        return tmp

    def setTableau(self, ligne, colonne, valeur):
        position = (ligne-1)*self.taille + colonne -1
        print( " ({},{}) = {} - position {}".format(ligne, colonne, valeur, position))
        self.tableau[position] = valeur

    def getTableau(self, ligne, colonne):
        position = (ligne-1)*self.taille + colonne -1
        print("get ({},{}) = {}".format(ligne, colonne, position))
        return self.tableau[position]

    def calcule_carre(self):
        c1 = 0
        colonne = int(self.taille/2)+1
        ligne =1

        flag = True

        while(flag):
            c1 = c1 + 1
            self.setTableau(ligne, colonne, c1)
            if (c1 == self.taille**2):
                flag =False
            elif c1%self.taille != 0 :
                colonne += 1
                if colonne <= self.taille:
                    ligne -= 1
                    if ligne <0 :
                        ligne = self.taille
                else:
                    colonne = 1
                    ligne -= 1
            else:
                ligne += 1

        t=0
        for i in range(1, self.taille+1):
            t = t + self.getTableau(i, 1)
        self.setTableau(1,0, t) 

print("="*30)
print("\tCarrés magiques")
print("="*30)

taille = choix_taille()
mon_carre =  magic(taille)

print(mon_carre)

mon_carre.calcule_carre()

print(mon_carre)