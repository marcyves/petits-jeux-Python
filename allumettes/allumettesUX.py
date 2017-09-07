#! /usr/bin/python

import os
import time
import pygame
from pygame.locals import *

"""
Petit jeu d'allumettes
-----------------------
Au départ il y a 30 allumettes, 2 joueurs prennent des à allumettes à tour de rôle.
Celui qui prend la dernière a perdu.
Chaque joueur peut prendre entre 1 et le double du nombre d'allumettes
prises par le précédent.

(c) Marc Augier 2016
    m.augier@me.com

"""

def load_image2(name, colorkey=None):
    fullname = os.path.join(name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error:
        print ('Cannot load image:', name)
        raise SystemExit
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

class allumette():
    """
    La classe allumette contient l'ensemble des fonctions du jeu.

    à l'initialisation, on passe le nombre d'allumettes du jeu
    En revanche la limite du premier retrait est fixée à 2
    """
    def __init__(self, n):
        self.allumettes = n
        self.limit = 2

    def retire(self, nb):
        """
        Méthode pour gérer un coup.
        C'est à dire retirer nb allumettes et mettre à jour la limite du coup suivant
        """
        retrait = min(nb, self.limit)
        self.allumettes -= retrait
        self.limit = 2*retrait
        if (self.allumettes > 0):
            return True
        else:
            return False

    def fin(self):
        """
        Méthode pour tester qu'il y a au moins une allumette en jeu
        """
        if (self.allumettes > 0):
            return True
        else:
            return False


    def joueur(self):
        """
        Le tour du joueur
        La méthode renvoie le nombre d'allumettes retirées par le joueur
        """

        ret = 1
        wait  = True

        while wait:
            dessine_plateau(ret,"vous pouvez", "Flèches haut et bas pour modifier, droite pour continuer")
#        ret = eval(input("Combien d'allumettes vous voulez retirer ? ==> "))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                elif event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_UP :
                        if ret < self.limit :
                            ret += 1
                    elif event.key == pygame.K_DOWN :
                        if ret > 1:
                            ret -= 1
                    elif event.key == pygame.K_RIGHT:
                        wait  = False

        return ret

    def ordi(self):
        """
        Le tour de l'ordinateur
        La méthode renvoie le nombre d'allumettes retirées par l'ordi

        L'IA du jeu (^_^);
        """
        dessine_plateau(1,"je peux", "")
        if self.allumettes == 1 :
            # Plus qu'une allumette, l'ordi a perdu
            # mais il est fair play et laisse un petit message
            nb = 1
            dessine_plateau(1,"je peux", "Bien joué")
        elif self.limit >= (self.allumettes-1):
            # L'ordi a détecté un coup gagnant, il ne laisse qu'une allumette
            nb = self.allumettes-1
            dessine_plateau(nb,"je peux", "Je crois que vous êtes mal parti...")
        else :
            # L'ordi se crée une situation gagnante
            # Il prend un nombre d'allumettes
            # - qui ne permet pas au joueur de gaganer
            # - qui devrait mettre le joueur en difficulté
            laisse = 2 * (self.limit+1)
            nb = max(1,min(self.limit,self.allumettes - laisse))

        dessine_plateau(nb,"je peux", "A mon tour, je retire %i " % nb)

        wait  = True
        while wait:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                elif event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_RIGHT:
                        wait  = False

        return nb

def rejoueOuQuitte():
    pygame.event.clear()
    for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]) :
        if event.type == pygame.QUIT :
            return False
        elif event.type == pygame.KEYUP or event.type == pygame.KEYDOWN :
            if event.key == K_q :
                return False
            else :
                return True
    return False

def creaTexteObj(texte, Police):
    texteSurface = Police.render(texte, True, white)
    return texteSurface, texteSurface.get_rect()

def gameOver(msg):
    GOTexte =  pygame.font.Font('BradBunR.ttf', 150)
    petitTexte =  pygame.font.Font('BradBunR.ttf', 20)

    GOTexteSurf, GOTexteRect = creaTexteObj(msg, GOTexte)
    petitTexteSurf, petitTexteRect = creaTexteObj("appuyer sur une touche pour continuer", petitTexte)

    GOTexteRect.center = surfaceW/2, ((surfaceH/2)-50)
    surface.blit(GOTexteSurf, GOTexteRect)

    petitTexteRect.center = surfaceW/2, ((surfaceH/2)+50)
    surface.blit(petitTexteSurf, petitTexteRect)

    pygame.display.update()

def score(compte):
    police =  pygame.font.Font('BradBunR.ttf', 16)
    texte = police.render("Score : "+str(compte), True, white)
    surface.blit(texte,[10,0])

def dessine(x, y, image):
    surface.blit(image, (x,y))

def dessine_plateau(retire, status, msg):

    # On dessine le tapis
    surface.fill(couleur_tapis)

    # On dessine les allumettes
    x0 = 20
    xstep = 20
    xmax = x0 + 30 * xstep
    compteur = 0
    y0 = 210
    ymax = 260

    y = y0
    for x in range(x0, xmax, xstep):
        compteur += 1
        dessine(x,y,img)
        if (compteur >= monJeu.allumettes):
            x = xmax
            y = ymax

# On affiche le compteur des allumettes à retirer
    compteurRetire =  pygame.font.Font('BradBunR.ttf', 150)
    retireSurf, retireRect = creaTexteObj(str(retire), compteurRetire)
    retireRect.center = 380, 120
    surface.blit(retireSurf, retireRect)

# On affiche le status
    police =  pygame.font.Font('BradBunR.ttf', 28)
    texte = police.render("%s en retirer de 1 à %i" % (status, min(monJeu.limit,monJeu.allumettes)), True, white)
    surface.blit(texte,[10,0])

# On affiche le message
    police =  pygame.font.Font('BradBunR.ttf', 28)
    texte = police.render("%s" % (msg), True, white)
    surface.blit(texte,[10,30])


    pygame.display.update()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Le programme commence ici
#
# On peut choisi un nombre d'allumettes de départ à la création de l'instance


# Initialisations
pygame.init()

surfaceW = 800
surfaceH = 600
white = (255,255,255)
couleur_tapis = (0,128,0)

img = pygame.image.load('allumette.png')

surface = pygame.display.set_mode((surfaceW,surfaceH))
pygame.display.set_caption("Le jeu des allumettes")

horloge = pygame.time.Clock()

def main():
    global monJeu

    monJeu = allumette(30)

    while (monJeu.fin()):

        retire = monJeu.joueur()
        retour = monJeu.retire(retire)

        pygame.event.clear()
        event = pygame.event.wait()

        if retour:
            retire = monJeu.ordi()
            retour = monJeu.retire(retire)
            if not retour:
                gameOver("Vous avez gagné !")
        else:
            gameOver("J'ai gagné !")
        pygame.display.update()


rejoue = True
while rejoue :
    main()
    time.sleep(1)
    horloge.tick()
    rejoue = rejoueOuQuitte()

pygame.quit()
quit()
