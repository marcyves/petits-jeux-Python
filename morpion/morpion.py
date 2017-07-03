#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
"""
Petit jeu de morpion
-----------------------
Une grille 3x3 et chaque joueur à tour de rôle va pose un pion,
représenté par un O ou un X.
Le premier qui aligne 3 pions a gagné !

(c) Marc Augier 2017
    m.augier@me.com

"""
def affiche_jeu(table_jeu):
    print ("  " + table_jeu[1] + " | " + table_jeu[2] + " | " + table_jeu[3] + "")
    print (" -----------")
    print ("  " + table_jeu[4] + " | " + table_jeu[5] + " | " + table_jeu[6] + "")
    print (" -----------")
    print ("  " + table_jeu[7] + " | " + table_jeu[8] + " | " + table_jeu[9] + "")

def jeu_joueur():
    """
    gestion du coup du joueur, question et vérifications
    """
    coup_joueur = raw_input("Où est-ce que vous placez votre pion ?  ")
    return

def jeu_ordi():
    """
    Ici l'IA du jeu ordinateur
    """
    print("À moi de jouer")
    
    return

def jeu_termine():
    return True

print("Petit jeu de morpion")
print("--------------------")
print("\n\n")

table_jeu = ["", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

print("Choisissez votre pion pour décider qui commence (O)")

pion_joueur = ""
while (pion_joueur != "O" and pion_joueur != "X"):
    pion_joueur = raw_input("Est-ce que vous jouez O ou X ? ==>  ").upper()

if pion_joueur == "O":
    pion_ordi = "X"
else:
    pion_ordi = "O"

jeu_en_cours = True

if pion_ordi == "O":
    jeu_ordi()

while(jeu_en_cours):
    affiche_jeu(table_jeu)
    jeu_joueur()
    if jeu_termine():
        jeu_en_cours = False

    affiche_jeu(table_jeu)
    jeu_ordi()
    if jeu_termine():
        jeu_en_cours = False

print("C'est terminé")
