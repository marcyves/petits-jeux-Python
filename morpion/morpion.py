#! /usr/bin/python
# -*- coding: utf-8 -*-

# version Python 2.x

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
        if  table_jeu[coup_joueur] != str(coup_joueur):
            print("Coup invalide, la case est prise")
            coup_joueur = 0
    table_jeu[coup_joueur] = pion_joueur
    return

def cherche_position_gagnante(pion):
    if (table_jeu[1] == pion and table_jeu[2] == pion and table_jeu[3] == "3" ):
        return 3
    if (table_jeu[1] == pion and table_jeu[2] == "2"  and table_jeu[3] == pion ):
        return 2
    if (table_jeu[1] == "1"  and table_jeu[2] == pion and table_jeu[3] == pion ):
        return 1
    if (table_jeu[4] == "4"  and table_jeu[5] == pion and table_jeu[6] == pion ):
        return 4
    if (table_jeu[4] == pion and table_jeu[5] == "5"  and table_jeu[6] == pion ):
        return 5
    if (table_jeu[4] == pion and table_jeu[5] == pion and table_jeu[6] == "6" ):
        return 6
    if (table_jeu[7] == "7" and table_jeu[8] == pion and table_jeu[9] == pion ):
        return 7
    if (table_jeu[7] == pion and table_jeu[8] == "8" and table_jeu[9] == pion ):
        return 8
    if (table_jeu[7] == pion and table_jeu[8] == pion and table_jeu[9] == "9" ):
        return 9
    if (table_jeu[1] == "1" and table_jeu[4] == pion and table_jeu[7] == pion ):
        return 1
    if (table_jeu[1] == pion and table_jeu[4] == "4" and table_jeu[7] == pion ):
        return 4
    if (table_jeu[1] == pion and table_jeu[4] == pion and table_jeu[7] == "7" ):
        return 7
    if (table_jeu[2] == "2" and table_jeu[5] == pion and table_jeu[8] == pion ):
        return 2
    if (table_jeu[2] == pion and table_jeu[5] == "5" and table_jeu[8] == pion ):
        return 5
    if (table_jeu[2] == pion and table_jeu[5] == pion and table_jeu[8] == "8" ):
        return 8
    if (table_jeu[3] == "3" and table_jeu[6] == pion and table_jeu[9] == pion ):
        return 3
    if (table_jeu[3] == pion and table_jeu[6] == "6" and table_jeu[9] == pion ):
        return 6
    if (table_jeu[3] == pion and table_jeu[6] == pion and table_jeu[9] == "9" ):
        return 9
    if (table_jeu[1] == "1" and table_jeu[5] == pion and table_jeu[9] == pion ):
        return 1
    if (table_jeu[1] == pion and table_jeu[5] == "5" and table_jeu[9] == pion ):
        return 5
    if (table_jeu[1] == pion and table_jeu[5] == pion and table_jeu[9] == "9" ):
        return 9
    if (table_jeu[7] == "7" and table_jeu[5] == pion and table_jeu[3] == pion ):
        return 7
    if (table_jeu[7] == pion and table_jeu[5] == "5" and table_jeu[3] == pion ):
        return 5
    if (table_jeu[7] == pion and table_jeu[5] == pion and table_jeu[3] == "3" ):
        return 3
    return 0

def jeu_ordi():
    """
    Ici l'IA du jeu ordinateur
    """
    print("\nÀ moi de jouer")
    # L'ordi cherche d'abord une position gagnante pour lui
    coup_ordi = cherche_position_gagnante(pion_ordi)
    if coup_ordi == 0:
        # ensuite il vérifie que le joueur n'est pas en position de gagner
        coup_ordi = cherche_position_gagnante(pion_joueur)
        if coup_ordi == 0:
            # reste à voir si le centre est encore libre
            if table_jeu[5] == "5":
                coup_ordi = 5
            else :
                # Sinon cherche le premier endroit libre
                for i in range(10):
                    if (table_jeu[i]== str(i)):
                        coup_ordi = i
                        break
    table_jeu[coup_ordi] = pion_ordi
    print("Je pose mon pion en " + str(coup_ordi))
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
        if pion == pion_joueur:
            print("\n\tBravo, vous avez gagné !")
        else:
            print("\n\tJ'ai gagné ! Bienvenue dans la matrice...")
        return True
    else:
        for i in range(10):
            if table_jeu[i] == str(i):
                return False
        print("\n\tMatch nul...")
        return True


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Le programme commence ici
#
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
        jeu_en_cours = False
    else:
        affiche_jeu(table_jeu)
        jeu_ordi()
        if jeu_termine(pion_ordi):
            jeu_en_cours = False

print("\nC'est terminé\n")
affiche_jeu(table_jeu)
