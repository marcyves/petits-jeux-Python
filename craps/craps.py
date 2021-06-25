#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
CRAPS
-----

Jeu de craps

"""
from random import randint

class craps:

    def __init__(self, p):
        self.portefeuille = p
        self.jouer = True
        self.mise = 0
        self.dé1 = 0
        self.dé2 = 0
        self.tour = 1
        self.cible = 0

        print("+-------------+")
        print("+  C R A P S  +")
        print("+-------------+\n")

        print("L'ordinateur lance les dés.\nSi au premier lancé vous obtenez 7 ou 11, vous doublez votre mise.")
        print("Si vous obtenez 2, 3 ou 12 vous perdez")
        print("Pour toute aure valeur vous relancez les dés, jusqu'à obtenir la même valeur de nouveau, ce qui doublera votre mise")
        print("Si dans l'intervalle vous obtenez un 7, vous perdez.\n")

    def en_cours(self):
        return self.jouer

    def miser(self):
        mise = 0
        
        print("Vous avez {} en portefeuille.".format(self.portefeuille))
        if self.tour >1:
            print("\tVous devez réaliser {} pour gagner".format(self.cible))
        
        while(mise<=0 or mise > self.portefeuille):
            try:
                mise = int(input("Combien vous voulez miser ? => "))
            except ValueError:
                print("\n\t\tMerci de rentrer une valeur numérique\n")
                mise = 0
        self.mise = mise
        self.portefeuille -= mise

    def lancer(self):
        self.dé1 = randint(1,6)
        self.dé2 = randint(1,6)

    def analyse(self):
        valeur = self.dé1+self.dé2
        print("Vous avez tiré {} et {}, ce qui fait {}".format(self.dé1, self.dé2, valeur))
        if self.tour == 1:
            if valeur == 7 or valeur == 11:
                self.gagne()
            elif valeur == 2 or valeur == 3 or valeur == 12:
                self.perdu()
            elif self.portefeuille == 0:
                print("\nVous êtes ruiné")
                self.perdu()
            else:
                self.tour += 1
                self.cible = valeur
        else:
            if valeur == 7:
                self.perdu()
            elif valeur == self.cible:
                self.gagne()
            elif self.portefeuille == 0:
                print("\nVous êtes ruiné")
                self.perdu()
    
    def gagne(self):
        print("Vous avez gagné")
        self.portefeuille += 2*self.mise
        print("Vous avez maintenant {} dans votre portefeuille".format(self.portefeuille))
        self.jouer =False

    def perdu(self):
        print("Vous avez perdu")
        print("Vous avez maintenant {} dans votre portefeuille".format(self.portefeuille))
        self.jouer =False

    def relance(self):
        self.jouer = True
        self.cible = 0
        self.tour  = 1

jeu = craps(200)

nouveau_tour = True

while nouveau_tour:
    jeu.miser()
    while jeu.en_cours():
        jeu.lancer()
        jeu.analyse()
    
    if jeu.portefeuille > 0:
        rep = ""
        while rep != "oui" and rep != "non":    
            rep = input("Continuer ? (oui, non) ")
        
        if rep == "non":
            nouveau_tour = False
        else:
            jeu.relance()
    else:
        nouveau_tour = False

print("\n\tAu revoir...")