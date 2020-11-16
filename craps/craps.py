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

        print("\n+-------------+")
        print("|  C R A P S  |")
        print("+-------------+")

        self.portefeuille = p
        self.mise = 0
        self.tour = 1
        self.cible = 0
        self.joue = True

    def affiche_regles(self):
        print("""Le Craps est un jeu de dés populaire en Amérique du Nord""")

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
        
        def jeuGagne(self):
            print("\n => Vous avez gagné {} ".format(2*self.mise))
            self.portefeuille += 2*self.mise
            rep = input("\nOn relance les dès (entrée pour continuer)")

        def jeuPerdu(self):
            print("\n => Vous avez perdu !")      
            self.fin()

        def debut(self):
            self.tour = 1
            self.cible = 0
            self.joue = True

        def fin(self):
            self.joue = False

        def getCible(self):
            return self.cible
        
        def setCible(self, c):
            self.cible = c

        def enCours(self):
            if self.portefeuille > 0:
                return self.joue
            else:
                return False

        def miser(self):
            mise = 0
            while(mise<=0 or mise > self.portefeuille) and self.getJoue():
                rep=input("\nVous avez {} en poche. Combien vous voulez miser ? (stop pour arrêter) ==> ".format(self.portefeuille))
                try:
                    mise = int(rep)
                except ValueError:
                    if rep == "stop":
                        self.fin()
                    else:
                        print("\t\tMerci d'entrer une valeur numérique")
                        mise = 0
            self.mise = mise
            self.portefeuille -= mise

        def lancer(self):
            return randint(1,6)

        def analyse(self, v1, v2):
            valeur = v1 + v2
            print("\n---> Vous avez tiré : {} et {}, ce qui fait {}".format(v1, v2, valeur))
            if self.tour == 1:
                if valeur==7 or valeur==11:
                    self.jeuGagne()
                elif valeur==2 or valeur==3 or valeur==12:
                    self.jeuPerdu()
                else:
                    self.tour += 1
                    self.setCible(valeur)
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
    while jeu.en_cours():
        jeu.miser()
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