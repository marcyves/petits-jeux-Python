#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
import time
import pygame
from pygame.locals import *

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
        self.table_jeu     = ["", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.pion_joueur   = ""
        self.pion_ordi     = ""
        self.a_qui_le_tour = ""
        self.message_final = ""

    
    def choix_pion(self):

        game_over = False
        wait  = True

        image = img_pion_cercle
        self.pion_joueur = "O"
        liste_messages = ["Bienvenue dans le jeu de morpion.", "Choisissez votre pion en utilisant les ", "flèches haut et bas pour le sélectionner.", "Flèche droite pour continuer", "Flèche gauche pour arrêter"]
        y = dessine_plateau("Petit jeu de Morpion", liste_messages)
        fenetre.blit(image, (500,80))
        pygame.display.update()

        while wait:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    wait  = False
                    game_over = True
                elif event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN :
                        if self.pion_joueur == "O":
                            self.pion_joueur = "X"
                            image = img_pion_croix
                        else:
                            self.pion_joueur = "O"
                            image = img_pion_cercle
                        fenetre.blit(image, (500,80))
                        pygame.display.update()
                    elif event.key == pygame.K_RIGHT:
                        wait  = False
                    elif event.key == pygame.K_LEFT:
                        wait  = False
                        game_over = True


        if self.pion_joueur == "O":
            self.pion_ordi = "X"
            self.a_qui_le_tour = "joueur"
        else:
            self.pion_ordi = "O"
            self.a_qui_le_tour = "ordi"

        return game_over

    def tour_de_jeu(self):
        jeu_en_cours = True

        self.affiche_jeu(["C'est parti !"])
    
        while(jeu_en_cours):
    
            for event in pygame.event.get():
                if event.type == QUIT:
                    jeu_en_cours = False
                if self.a_qui_le_tour == "ordi":
                    self.jeu_ordi()
                    self.a_qui_le_tour = "joueur"
                    self.affiche_jeu(["À vous de jouer !"])
                else:
                    if event.type == MOUSEBUTTONDOWN and event.button == 1 :
                        clic_x = event.pos[0]
                        clic_y = event.pos[1]
                        coup_joueur = renvoie_pion(clic_x, clic_y)

                        if coup_joueur > 0:
                            self.table_jeu[coup_joueur] = self.pion_joueur
                            self.a_qui_le_tour = "ordi"
                            self.affiche_jeu(["À moi de jouer !"])



            if self.jeu_termine(self.pion_joueur) or self.jeu_termine(self.pion_ordi):
                jeu_en_cours = False

    def affiche_jeu(self, liste_messages):
        y = dessine_plateau("Petit jeu de Morpion", liste_messages)

        x0 = 100
        y0 = max(120,y)
        step = 150

        fenetre.blit(renvoie_icone(self.table_jeu[1]), (x0,y0))
        fenetre.blit(renvoie_icone(self.table_jeu[2]), (x0+step,y0))
        fenetre.blit(renvoie_icone(self.table_jeu[3]), (x0+2*step,y0))
        fenetre.blit(renvoie_icone(self.table_jeu[4]), (x0,y0+step))
        fenetre.blit(renvoie_icone(self.table_jeu[5]), (x0+step,y0+step))
        fenetre.blit(renvoie_icone(self.table_jeu[6]), (x0+2*step,y0+step))
        fenetre.blit(renvoie_icone(self.table_jeu[7]), (x0,y0+2*step))
        fenetre.blit(renvoie_icone(self.table_jeu[8]), (x0+step,y0+2*step))
        fenetre.blit(renvoie_icone(self.table_jeu[9]), (x0+2*step,y0+2*step))

        pygame.display.flip()

    
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
                self.message_final = "Bravo, vous avez gagné !"
            else:
                self.message_final = "J'ai gagné ! Bienvenue dans la matrice..."
            return True
        else:
            for i in range(10):
                if self.table_jeu[i] == str(i):
                    return False
            self.message_final = "Match nul..."
            return True


def rejoueOuQuitte():
    pygame.event.clear()
    wait  = True

    liste_messages = []
    liste_messages.append(partie.message_final)
    liste_messages.append("Voulez-vous recommencer ?")
    liste_messages.append("O/N ou Q pour quitter")
    partie.affiche_jeu(liste_messages)
    pygame.display.update()

    while wait:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                wait   = False
                rejoue = False
            elif event.type == pygame.KEYUP or event.type == pygame.KEYDOWN :
                if event.key == K_q :
                    wait   = False
                    rejoue = False
                elif event.key == K_o :
                    wait   = False
                    rejoue = True
                elif event.key == K_n:
                    wait   = False
                    rejoue = False
    return rejoue


def creaTexteObj(texte, Police):
    textefenetre = Police.render(texte, True, white)
    return textefenetre, textefenetre.get_rect()


def dessine_plateau(titre, liste_messages):

    # On dessine le tapis
    fenetre.fill(couleur_tapis)
    # On affiche le titre
    police =  pygame.font.Font('BradBunR.ttf', 28)
    texte = police.render(titre, True, white)
    fenetre.blit(texte,[30,30])

    # On affiche les messages
    y = 80
    police =  pygame.font.Font('BradBunR.ttf', 28)
    for msg in liste_messages:
        texte = police.render("%s" % (msg), True, white)
        fenetre.blit(texte,[50,y])
        y += 30

    pygame.display.update()
    pygame.display.flip()
    y += 30

    return y


def renvoie_pion(x, y):
    x0 = 100
    y0 = 120
    step = 150

    x -= x0
    y -= y0

    if x< 0 or x > 3*step:
        return 0
    if y <0 or y > 3*step:
        return 0

    tmp = x//step + 1 + (y//step) * 3

    return tmp


def renvoie_icone(pion):
    if pion == "O":
        tmp = img_pion_cercle
    elif pion == "X":
        tmp = img_pion_croix
    else:
        tmp = img_vide
    return tmp

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Le programme commence ici
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

if __name__ == "__main__":

    FRAMERATE = 60
    largeur = 700
    hauteur = 700
    white = (255,255,255)
    couleur_tapis = (0,128,0)

    pygame.init()

    fenetre = pygame.display.set_mode((largeur,hauteur))
    pygame.display.set_caption("Petit Jeu de Morpion")

    img_pion_cercle = pygame.image.load('cercle.png').convert_alpha()
    img_pion_croix  = pygame.image.load('croix.png').convert_alpha()
    img_vide        = pygame.image.load('vide.png').convert_alpha()
    img_plateau     = pygame.image.load('plateau.png').convert_alpha()

    horloge = pygame.time.Clock().tick(FRAMERATE)

    rejoue = True
    while rejoue :
        partie = morpion()

        if partie.choix_pion():
            rejoue = False
        else:
            partie.tour_de_jeu()

        rejoue = rejoueOuQuitte()

    pygame.quit()
    quit()
