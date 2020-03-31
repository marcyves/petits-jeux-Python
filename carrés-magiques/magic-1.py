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

    def calcule_carre(self):
        pass

    def affiche_carre(self):
        pass

def choix_taille():
    return 5

# Le programme commence ici
if __name__ == "__main__":
    print("Carrés magiques")

    taille = choix_taille()

    mon_carre = carreMagique(taille)

    mon_carre.calcule_carre()
    mon_carre.affiche_carre()