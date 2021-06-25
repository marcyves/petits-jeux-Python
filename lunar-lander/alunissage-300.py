#! /usr/bin/python
# -*- coding: utf-8 -*-

import signal
import matplotlib.pyplot as plt
from rich import print

TIMEOUT = 5

def interrupted(signum, frame):
    "called when read times out"
    raise TropLent
signal.signal(signal.SIGALRM, interrupted)

class TropLent(Exception):
    pass

class Module():

    def __init__(self, altitude, vitesse, carburant, poussée, pousséeMax):
        self.altitude   =  altitude
        self.vitesse    =  vitesse
        self.carburant  =  carburant
        self.poussée    =  poussée
        self.pousséeMax =  pousséeMax


    def getAltitude(self):
        return self.altitude

    def getVitesse(self):
        return self.vitesse

    def getCarburant(self):
        return self.carburant

    def getPoussée(self):
        return self.poussée

    def getPousséeMax(self):
        return self.pousséeMax

    def setAltitude(self, altitude):
        if altitude < 0:
            altitude = 0
        self.altitude = altitude

    def monte(self, q):
        self.altitude += q

    def setVitesse(self, vitesse):
        self.vitesse = vitesse

    def setCarburant(self, carburant):
        self.carburant = carburant

    def bruleCarburant(self, carburant):
        if carburant > self.carburant:
            carburant = self.carburant
        self.carburant -= carburant
 
        poussée = (self.poussée//2 + carburant)//2

        return poussée

    def setPoussée(self, poussée):
        self.poussée = poussée
    
    def setPousséeMax(self, poussée):
        self.pousséeMax = poussée

class Alunissage():

    def __init__(self):
        self.étape       =   1
        self.heure       =   0
        self.gravitation = 100
        self.carburant_précédent = 0
        self.trajectoire = []
        self.niveau      = ""

        self.niveaux = {'Facile':[
            1,          # numéro du niveau
            5000,       # Altitude de départ
            1000,       # Vitesse initiale
            6000,       # Carburant
            200,        # Poussée initiale
            500         # Poussée Max
        ],
        'Basse altitude':[2, 2000, 800, 3000, 200 , 400],
        'Peu de carburant':[3, 3000, 600, 3000, 0, 500],
        'Haute altitude':[4, 10000, 1000, 6000, 500, 500]
        }

    def choixNiveau(self):

        print("\nLes niveaux disponibles\n")

        for niveau in self.niveaux:
            print("\t{} - {}".format(self.niveaux[niveau][0], niveau))

        n = 0
        while (n<1 or n>len(self.niveaux)):
            try:
                n = int(input("\nQuel niveau vous voulez [1]/{} => ".format(len(self.niveaux))))
            except:
                n = 1

        for niveau in self.niveaux:
            if self.niveaux[niveau][0] == n:
                self.niveau = niveau
                altitude   = self.niveaux[niveau][1]
                vitesse    = self.niveaux[niveau][2]
                carburant  = self.niveaux[niveau][3]
                poussée    = self.niveaux[niveau][4]
                pousséeMax = self.niveaux[niveau][5]
                self.vaisseau = Module(altitude, vitesse, carburant, poussée, pousséeMax)
                break

        print("\nL'altitude du vaisseau en orbite est {}".format(self.vaisseau.getAltitude()))

    def enVol(self):
        if self.vaisseau.getAltitude()>0:
            return True
        else:
            return False

    def affichage(self, message):
        self.trajectoire.append(self.vaisseau.getAltitude())
        print("\n\t+------------------------------------+")
        print("\t|                 [yellow]{:>2}[/yellow]                 |".format(self.étape))
        print("\t+------------------------------------+")
        if self.vaisseau.getCarburant() <= 0:
            print("\t| {:^34} |".format("[bold red]Vous êtes à court de carburant ![/bold red] "))
            print("\t+------------------------------------+")
        print("\t| [cyan]{:^34}[/cyan] |".format(message))
        print("\t+------------------------------------+")
        print("\t| Altitude {:>5} m   Carburant {:>5} |".format(self.vaisseau.getAltitude(), self.vaisseau.getCarburant()))
        print("\t| Vitesse  {:>5} m/s Poussée   {:>5} |".format(self.vaisseau.getVitesse(), self.vaisseau.getPoussée()))
        print("\t+------------------------------------+")

    def pilotage(self):
        carburant = -1

        signal.alarm(TIMEOUT)

        while(carburant<0 or carburant>self.vaisseau.getPousséeMax()):
            try:
                carburant = int(input("\nCombien bruler de carburant (max={:<3}) ==> ".format(self.vaisseau.getPousséeMax())))
            except ValueError:
               carburant = 0
            except TropLent:
                print(self.carburant_précédent)
                print("\n[red]Vous êtes trop lent à répondre[/red]")
                carburant = self.carburant_précédent

        signal.alarm(0)

        poussée = self.vaisseau.bruleCarburant(carburant)
        self.carburant_précédent = carburant
        self.vaisseau.setPoussée(poussée)

    def simulation(self):
        self.étape += 1
        
        vitesse = self.vaisseau.getVitesse() + self.gravitation - self.vaisseau.getPoussée()
        altitude0 = self.vaisseau.getAltitude()
        altitude1 = altitude0 - vitesse

        self.vaisseau.setAltitude(altitude1)
        self.vaisseau.setVitesse(vitesse)

        if altitude1>altitude0:
            msg = "Le vaisseau monte"
        elif altitude1 == altitude0:
            msg = "Vous êtes en orbite stationnaire"
        else:
            msg = "Le vaisseau descend"

        return msg

    def resultat(self):
        v = self.vaisseau.getVitesse()

        if v > 100:
            print("\nLe vaisseau s'est fracassé, il n'y a pas de survivant.")
        elif v > 30:
            print("\nLe vaisseau s'est posé brutalement, pas sûr que vous puissiez redécoller.")
        else:
            print("\nBravo, alunissage parfaitement réussi !") 
        print("\nGame over")
    
    def displayTrajectoire(self):
        plt.title("Votre alunissage\nNiveau {}".format(self.niveau))
        x = range(len(self.trajectoire))
        plt.scatter(x, self.trajectoire)
        plt.show()
                    
if __name__ == "__main__":
    print("Alunissage")
    print("----------\n")

    jeu = Alunissage()

    jeu.choixNiveau()

    message = "C'est parti !"
    while jeu.enVol():
        jeu.affichage(message)
        jeu.pilotage()
        message = jeu.simulation()

    jeu.affichage("Game Over")
    jeu.resultat()
    jeu.displayTrajectoire()

