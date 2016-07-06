#! /usr/bin/python

import sys
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
class allumette():
    """
    La classe allumette contient l'ensemble des fonctions du jeu.

    à l'initialisation, on passe le nombre d'allumettes du jeu
    En revanche la limite du premier retrait est fixée à 2
    """
    def __init__(self, n):
        self.allumettes = n
        self.limit = 2

    def afficheStatut(self, text):
        """
        Méthode qui permet d'afficher à quel niveau du jeu nous sommes
        Elle reçoit en variable texte une chaine différente suivant
         que nous sommes dans le tour du joueur ou celui de l'ordi
        """
        print ("\nIl y a %i allumettes et %s en retirer de 1 à %i" % (self.allumettes, text, min(self.limit,self.allumettes)))


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
        ret = 0
        while (ret < 1 or ret > self.limit):
            self.afficheStatut("vous pouvez")
            ret = eval(input("Combien d'allumettes vous voulez retirer ? ==> "))
        return ret

    def ordi(self):
        """
        Le tour de l'ordinateur
        La méthode renvoie le nombre d'allumettes retirées par l'ordi

        L'IA du jeu (^_^);
        """
        self.afficheStatut("je peux")
        if self.allumettes == 1 :
            # Plus qu'une allumette, l'ordi a perdu
            # mais il est fair play et laisse un petit message
            nb = 1
            print("Bien joué")
        elif self.limit >= (self.allumettes-1):
            # L'ordi a détecté un coup gagnant, il ne laisse qu'une allumette
            nb = self.allumettes-1
            print("Je crois que vous êtes mal parti...")
        else :
            # L'ordi se crée une situation gagnante
            # Il prend un nombre d'allumettes
            # - qui ne permet pas au joueur de gaganer
            # - qui devrait mettre le joueur en difficulté
            laisse = 2 * (self.limit+1)
            nb = max(1,min(self.limit,self.allumettes - laisse))

        print("A mon tour, je retire %i " % nb)
        return nb

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Le programme commence ici
#
# On peut choisi un nombre d'allumettes de départ à la création de l'instance
monJeu = allumette(30)

while (monJeu.fin()):
    retire = monJeu.joueur()
    retour = monJeu.retire(retire)
    if retour:
        retire = monJeu.ordi()
        retour = monJeu.retire(retire)
        if not retour:
            print("Vous avez gagné !")
    else:
        print("J'ai gagné !")

print("C'est terminé")
