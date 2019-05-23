#! /usr/bin/python
# -*- coding: utf-8 -*-
"""
Craps
-----

Le Craps est un jeu de dés populaire en Amérique du Nord

L'ordinateur lance les dés, si au premier lancé vous obtenez 7 ou 11, vous doublez votre mise. Si vous obtenez 2, 3 ou 12, vous perdez.
Pour toute autre valeur, vous relancez les dés, jusqu'à obtenir la même valeur de nouveau, ce qui doublera votre mise.
Mais si dans l'intervalle vous obtenez un 7, vous perdez.

(c) Marc Augier 2019
    m.augier@me.com
"""
from random import randint

class craps:
        def __init__(self, p):

            print("===============")
            print("=  C R A P S  =")
            print("===============")

            self.portefeuille = p
            self.mise = 0

        def affiche_regles(self):
            print("""Le Craps est un jeu de dés populaire en Amérique du Nord

            L'ordinateur lance les dés, si au premier lancé vous obtenez 7 ou 11, vous doublez votre mise. Si vous obtenez 2, 3 ou 12, vous perdez.
            Pour toute autre valeur, vous relancez les dés, jusqu'à obtenir la même valeur de nouveau, ce qui doublera votre mise.
            Mais si dans l'intervalle vous obtenez un 7, vous perdez.
            """)
        
        def en_cours(self):
            if self.portefeuille > 0:
                return True
            else:
                return False

        def miser(self):
            mise = 0
            while(mise<=0 and mise <= self.portefeuille):
                mise=input("Vous avez {} en poche\nCombien vous voulez miser ? ==> ".format(self.portefeuille))
                try:
                    mise = int(mise)
                except ValueError:
                    print("\t\tMerci d'entrer une valeur numérique")
            self.mise = mise
            self.portefeuille -= mise

        def lancer(self):
            des = randint(1,6)
            

                    


jeu = craps(500)

jeu.affiche_regles()

while (jeu.en_cours()):
    jeu.miser()
    jeu.lancer()