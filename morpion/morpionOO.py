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

class morpion:
    def __init__(self):
        self.table_jeu   = ["", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.pion_joueur = ""
        self.pion_ordi   = ""

        print("\n\tPetit jeu de morpion")
        print("\t--------------------")
        print("\n\n")

    def choix_pion(self):

        print("Choisissez votre pion pour décider qui commence (O)")

        while (self.pion_joueur != "O" and self.pion_joueur != "X"):
            self.pion_joueur = input("Est-ce que vous jouez O ou X ? ==>  ").upper()

        if self.pion_joueur == "O":
            self.pion_ordi = "X"
        else:
            self.pion_ordi = "O"
            # L'ordinateur joue son premier coup
            self.jeu_ordi()

    def tour_de_jeu(self):
        jeu_en_cours = True

        while(jeu_en_cours):
            self.affiche_jeu()
            self.jeu_joueur()
            if self.jeu_termine(self.pion_joueur):
                jeu_en_cours = False
            else:
                self.affiche_jeu()
                self.jeu_ordi()
                if self.jeu_termine(self.pion_ordi):
                    jeu_en_cours = False

    def affiche_jeu(self):
        print ("  " + self.table_jeu[1] + " | " + self.table_jeu[2] + " | " + self.table_jeu[3] + "")
        print (" -----------")
        print ("  " + self.table_jeu[4] + " | " + self.table_jeu[5] + " | " + self.table_jeu[6] + "")
        print (" -----------")
        print ("  " + self.table_jeu[7] + " | " + self.table_jeu[8] + " | " + self.table_jeu[9] + "")

    def cherche_position_gagnante(self, pion):
        if (self.table_jeu[1] == pion and self.table_jeu[2] == pion and self.table_jeu[3] == "3" ):
            return 3
        if (self.table_jeu[1] == pion and self.table_jeu[2] == "2"  and self.table_jeu[3] == pion ):
            return 2
        if (self.table_jeu[1] == "1"  and self.table_jeu[2] == pion and self.table_jeu[3] == pion ):
            return 1
        if (self.table_jeu[4] == "4"  and self.table_jeu[5] == pion and self.table_jeu[6] == pion ):
            return 4
        if (self.table_jeu[4] == pion and self.table_jeu[5] == "5"  and self.table_jeu[6] == pion ):
            return 5
        if (self.table_jeu[4] == pion and self.table_jeu[5] == pion and self.table_jeu[6] == "6" ):
            return 6
        if (self.table_jeu[7] == "7" and self.table_jeu[8] == pion and self.table_jeu[9] == pion ):
            return 7
        if (self.table_jeu[7] == pion and self.table_jeu[8] == "8" and self.table_jeu[9] == pion ):
            return 8
        if (self.table_jeu[7] == pion and self.table_jeu[8] == pion and self.table_jeu[9] == "9" ):
            return 9
        if (self.table_jeu[1] == "1" and self.table_jeu[4] == pion and self.table_jeu[7] == pion ):
            return 1
        if (self.table_jeu[1] == pion and self.table_jeu[4] == "4" and self.table_jeu[7] == pion ):
            return 4
        if (self.table_jeu[1] == pion and self.table_jeu[4] == pion and self.table_jeu[7] == "7" ):
            return 7
        if (self.table_jeu[2] == "2" and self.table_jeu[5] == pion and self.table_jeu[8] == pion ):
            return 2
        if (self.table_jeu[2] == pion and self.table_jeu[5] == "5" and self.table_jeu[8] == pion ):
            return 5
        if (self.table_jeu[2] == pion and self.table_jeu[5] == pion and self.table_jeu[8] == "8" ):
            return 8
        if (self.table_jeu[3] == "3" and self.table_jeu[6] == pion and self.table_jeu[9] == pion ):
            return 3
        if (self.table_jeu[3] == pion and self.table_jeu[6] == "6" and self.table_jeu[9] == pion ):
            return 6
        if (self.table_jeu[3] == pion and self.table_jeu[6] == pion and self.table_jeu[9] == "9" ):
            return 9
        if (self.table_jeu[1] == "1" and self.table_jeu[5] == pion and self.table_jeu[9] == pion ):
            return 1
        if (self.table_jeu[1] == pion and self.table_jeu[5] == "5" and self.table_jeu[9] == pion ):
            return 5
        if (self.table_jeu[1] == pion and self.table_jeu[5] == pion and self.table_jeu[9] == "9" ):
            return 9
        if (self.table_jeu[7] == "7" and self.table_jeu[5] == pion and self.table_jeu[3] == pion ):
            return 7
        if (self.table_jeu[7] == pion and self.table_jeu[5] == "5" and self.table_jeu[3] == pion ):
            return 5
        if (self.table_jeu[7] == pion and self.table_jeu[5] == pion and self.table_jeu[3] == "3" ):
            return 3
        return 0

    def jeu_ordi(self):
        """
        Ici l'IA du jeu ordinateur
        """
        print("\nÀ moi de jouer")
        # L'ordi cherche d'abord une position gagnante pour lui
        coup_ordi = self.cherche_position_gagnante(self.pion_ordi)
        if coup_ordi == 0:
            # ensuite il vérifie que le joueur n'est pas en position de gagner
            coup_ordi = self.cherche_position_gagnante(self.pion_joueur)
            if coup_ordi == 0:
                # reste à voir si le centre est encore libre
                if self.table_jeu[5] == "5":
                    coup_ordi = 5
                else :
                    # Sinon cherche le premier endroit libre
                    for i in range(10):
                        if (self.table_jeu[i]== str(i)):
                            coup_ordi = i
                            break
        self.table_jeu[coup_ordi] = self.pion_ordi
        print("Je pose mon pion en " + str(coup_ordi))
        return

    def jeu_joueur(self):
        """
        gestion du coup du joueur, question et vérifications
        """
        coup_joueur = 0
        while (coup_joueur <= 0 or coup_joueur >9):
            coup_joueur = int(input("Où est-ce que vous placez votre pion ?  "))
            if  self.table_jeu[coup_joueur] != str(coup_joueur):
                print("Coup invalide, la case est prise")
                coup_joueur = 0
        self.table_jeu[coup_joueur] = self.pion_joueur
        return

    def jeu_termine(self, pion):
        """
        On teste si position gagnante
        """

        if ((self.table_jeu[1] == pion and self.table_jeu[2] == pion and self.table_jeu[3] == pion )
        or (self.table_jeu[4] == pion and self.table_jeu[5] == pion and self.table_jeu[6] == pion )
        or (self.table_jeu[7] == pion and self.table_jeu[8] == pion and self.table_jeu[9] == pion )
        or (self.table_jeu[1] == pion and self.table_jeu[4] == pion and self.table_jeu[7] == pion )
        or (self.table_jeu[2] == pion and self.table_jeu[5] == pion and self.table_jeu[8] == pion )
        or (self.table_jeu[3] == pion and self.table_jeu[6] == pion and self.table_jeu[9] == pion )
        or (self.table_jeu[1] == pion and self.table_jeu[5] == pion and self.table_jeu[9] == pion )
        or (self.table_jeu[7] == pion and self.table_jeu[5] == pion and self.table_jeu[3] == pion )):
            if pion == self.pion_joueur:
                print("\n\tBravo, vous avez gagné !")
            else:
                print("\n\tJ'ai gagné ! Bienvenue dans la matrice...")
            return True
        else:
            for i in range(10):
                if self.table_jeu[i] == str(i):
                    return False
            print("\n\tMatch nul...")
            return True

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Le programme commence ici
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
if __name__ == "__main__":
    partie = morpion()
    partie.choix_pion()

    partie.tour_de_jeu()

    print("\nC'est terminé\n")
    partie.affiche_jeu()
