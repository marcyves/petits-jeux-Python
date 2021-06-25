#! /usr/bin/python
# -*- coding: utf-8 -*-

"""

Acey Deucey
===========

Simulation du jeu de cartes Acey Deucey.

Librement inspiré du programme Basic https://www.atariarchives.org/basicgames/showpage.php?page=2 

(c) 2021 Marc Augier m.augier@me.com

"""
from random import randint

class AceyDucey:

    def __init__(self, porte_monnaie):
        print("\aAcey Deucey")
        print("====================\n")
        print("Acey-Deucey se joue de la manière suivante")
        print("L'ordinateur distribue 2 cartes faces découvertes")
        print("Tu as le choix entre miser ou pas suivant")
        print("que tu penses que la carte suivante aura")
        print("une valeur comprise entre les deux premières.\n")

        self.porte_monnaie_initial = porte_monnaie
        self.porte_monnaie = porte_monnaie
        self.jeu_terminé = False

        self.carte1 = 0
        self.carte2 = 0

    def mise(self):
        mise = -1

        print("\nIl te reste {} euros".format(self.porte_monnaie))
        while mise < 0 or mise > self.porte_monnaie:
            try:
                mise = int(input("\nQuelle est votre mise? (0 pour terminer) => "))
            except ValueError:
                mise = -1

        if mise > self.porte_monnaie:
            print("Désolé mon pote, tu as trop misé")
            print("Il ne te reste que {} euros à miser".format(self.porte_monnaie))
        elif mise == 0:
            print("Trouillard !!")

        return mise

    def gameOver(self):
        if self.porte_monnaie <= 0:
            self.jeu_terminé = True
            self.porte_monnaie = 0
            print("\nDésolé mon pote, tu es à sec")
        return self.jeu_terminé

    def displaycarte(self, carte):
        
        if carte < 11:
            print(carte)
        elif carte == 11:
            print("Valet")
        elif carte == 12:
            print("Reine")
        elif carte == 13:
            print("Roi")
        elif carte == 14:
            print("As")

    def draw(self):
        print("\nVoici les 2 cartes suivantes")
        
        self.carte1 = randint(2,14)
        self.carte2 = randint(2,14)

        if self.carte1 > self.carte2:
            self.carte1, self.carte2 = self.carte2, self.carte1

        self.displaycarte(self.carte1)
        self.displaycarte(self.carte2)

    def checkResult(self, carte, mise):
        if carte > self.carte1 and carte < self.carte2:
            print("Tu as gagné !!!")
            self.porte_monnaie += mise
        else:
            print("Désolé, tu as perdu")
            self.porte_monnaie -= mise
    
    def newGame(self):

        if self.porte_monnaie == 0:
            answer = ""
            while  answer.upper()[0:1] != "O" and  answer.upper()[0:1] != "N":
                answer = input("\nOn rejoue ? (Oui ou Non) => ")

            if  answer.upper()[0:1] == "O":
                self.porte_monnaie = self.porte_monnaie_initial
                self.jeu_terminé = False
                return True
            else:
                return False
        else:
            return True

if __name__ == "__main__":
    game = AceyDucey(100)
    
    while game.newGame():
        while not game.gameOver():
            game.draw()
            my_mise = game.mise()
            if my_mise != 0:
                my_carte = randint(2,14)
                game.displaycarte(my_carte)
                game.checkResult(my_carte, my_mise)

    print("Salut, j'espère que tu t'es bien amusé")
