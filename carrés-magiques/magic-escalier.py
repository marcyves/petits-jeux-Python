#! /usr/bin/python
# -*- coding: utf-8 -*-

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

class carreMagique:

    def __init__(self, taille):
        self.taille = taille
        self.tableau = [[0 for x in range(taille)] for x in range(taille)]

    def calcule_carre(self):
        ligne = 1
        col   = 3
        for valeur in range(1, (taille)**2+1):
            collision = False
            while(not self.setXYSafe(ligne, col, valeur)):
                #Debug print("Collision en {},{}".format(ligne,col))
                if collision:
                    ligne += 1                     
                else:
                    collision =True
                    ligne += 2
                    col   -= 1
                if ligne <= 0:
                    ligne = self.taille
                if col <= 0:
                    col = self.taille
                if ligne > self.taille:
                    ligne = 1
                if col > self.taille:
                    col = 1
            else:
                ligne -= 1
                col   += 1
            if ligne <= 0:
                ligne = self.taille
            if col <= 0:
                col = self.taille
            if ligne > self.taille:
                ligne = 1
            if col > self.taille:
                col = 1
            #Debug print("=> {},{}".format(ligne, col))


    def affiche_carre(self):
        print("-"*30)
        compteur = 0
        for i in range(1,self.taille + 1):
            compteur += self.getXY(i, 6-i)
        print("  {:>2d} =".format(compteur))
        print("-"*30)
        compteur = 0
        for ligne in range(1, self.taille + 1):
            print("  {:>2d}".format(ligne), end=" : ")
            for col in range(1, self.taille +1):
                print("{:>2d}".format(self.getXY(ligne, col)), end=" ")
                compteur += self.getXY(ligne, col)
            print("  = {}".format(compteur))
            compteur = 0
        print("-"*30)
        print("     : ", end='')
        compteur = 0
        for col in range(1, self.taille + 1):
            for ligne in range(1, self.taille +1):
                compteur += self.getXY(ligne, col)
            print(compteur, end=" ")
            compteur = 0
        compteur = 0
        for i in range(1,self.taille + 1):
            compteur += self.getXY(i, i)
        print("  = {}".format(compteur))
        print("-"*30)


    def getXY(self, x, y):
        x = x - 1
        y = y - 1
        return self.tableau[x][y]

    def setXY(self, x , y, valeur):
        print("Je mets {} en {},{}".format(valeur, x, y))
        x = x - 1
        y = y - 1
        self.tableau[x][y] = valeur

    def setXYSafe(self, x , y, valeur):
        #Debug print("Je mets {} en {},{}".format(valeur, x, y))
        x = x - 1
        y = y - 1
        if self.tableau[x][y] == 0:
            self.tableau[x][y] = valeur
            return True
        else:
            return False

def choix_taille():

    taille  = 0
    print("Choisissez la taille du carré")
    while (taille%2 == 0):
        taille = int(input("Entrez un nombre impair ==>  "))

    print("Calcul d'un carré de {}x{}".format(taille,taille))

    return taille

# Le programme commence ici
if __name__ == "__main__":
    print("")
    print("Carrés magiques")
    print("===============")
    print("")
    taille = choix_taille()

    mon_carre = carreMagique(taille)

    mon_carre.calcule_carre()
    mon_carre.affiche_carre()