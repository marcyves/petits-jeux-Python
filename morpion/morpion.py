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
    coup_joueur = 0
    while (coup_joueur <= 0 or coup_joueur >9):
        coup_joueur = input("Où est-ce que vous placez votre pion ?  ")
    table_jeu[coup_joueur] = pion_joueur
    return

def jeu_ordi():
    """
    Ici l'IA du jeu ordinateur
    """
    print("À moi de jouer")
    for i in range(10):
        if (table_jeu[i]== str(i)):
            table_jeu[i] = pion_ordi
            print("Je pose mon pion en " + str(i))
            break
    return

def jeu_termine(pion):
    """
    On teste si position gagnante
    """

    if ((table_jeu[1] == pion and table_jeu[2] == pion and table_jeu[3] == pion )
    or (table_jeu[4] == pion and table_jeu[5] == pion and table_jeu[6] == pion )
    or (table_jeu[7] == pion and table_jeu[8] == pion and table_jeu[9] == pion )
    or (table_jeu[1] == pion and table_jeu[4] == pion and table_jeu[7] == pion )
    or (table_jeu[2] == pion and table_jeu[5] == pion and table_jeu[8] == pion )
    or (table_jeu[3] == pion and table_jeu[6] == pion and table_jeu[9] == pion )
    or (table_jeu[1] == pion and table_jeu[5] == pion and table_jeu[9] == pion )
    or (table_jeu[7] == pion and table_jeu[5] == pion and table_jeu[3] == pion )):
        return True
    else:
        return False

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
    if jeu_termine(pion_joueur):
        print("Bravo, vous avez gagné !")
        jeu_en_cours = False
    else:
        affiche_jeu(table_jeu)
        jeu_ordi()
        if jeu_termine(pion_ordi):
            print("J'ai gagné ! Bienvenue dans la matrice...")
            jeu_en_cours = False

print("\nC'est terminé\n")
affiche_jeu(table_jeu)
