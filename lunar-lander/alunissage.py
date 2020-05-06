#! /usr/bin/python
# -*- coding: utf-8 -*-

class Module():

    def __init__(self):
        self.altitude   =  5000
        self.vitesse    =  1000
        self.carburant  =  4000
        self.poussée    =     0
        self.pousséeMax =   500

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
        self.altitude = altitude

    def monte(self, q):
        self.altitude += q

    def setVitesse(self, vitesse):
        self.vitesse = vitesse

    def setCarburant(self, carburant):
        self.carburant = carburant

    def bruleCarburant(self, carburant):
        self.carburant -= carburant
        if self.carburant < 0:
            self.carburant = 0
            print("ATTENTION: Vous êtes à court de carburant !")

    def setPoussée(self, poussée):
        self.poussée = poussée
    
    def setPousséeMax(self, poussée):
        self.pousséeMax = poussée

class Alunissage():

    def __init__(self):
        self.étape       =   1
        self.heure       =   0
        self.gravitation = 100
        self.vaisseau = Module()
        print("L'altitude du vaisseau en orbite est {}".format(self.vaisseau.getAltitude()))

    def enVol(self):
        if self.vaisseau.getAltitude()>0:
            return True
        else:
            return False

    def affichage(self):
        print("\n\t+------------------------------------+")
        print("\t| - - - - - - - - {} - - - - - - - - |".format(self.étape))
        print("\t| Altitude {} m   Carburant {} ".format(self.vaisseau.getAltitude(), self.vaisseau.getCarburant()))
        print("\t| Vitesse {} m/s".format(self.vaisseau.getVitesse()))
        print("\t| Poussée {} ".format(self.vaisseau.getPoussée()))
        print("\t+------------------------------------+")

    def pilotage(self):
        poussée = -1
        while(poussée<0 or poussée>self.vaisseau.getPousséeMax()):
            poussée = int(input("Combien bruler de carburant ==> "))
        self.vaisseau.bruleCarburant(poussée)
        self.vaisseau.setPoussée(poussée)

    def simulation(self):
        self.étape += 1
        
        vitesse = self.vaisseau.getVitesse() + self.gravitation - self.vaisseau.getPoussée()
        altitude0 = self.vaisseau.getAltitude()
        altitude1 = altitude0 - vitesse

        self.vaisseau.setAltitude(altitude1)
        self.vaisseau.setVitesse(vitesse)

        if altitude1>altitude0:
            print("\n\tLe vaisseau monte")
        elif altitude1 == altitude0:
            print("\n\tVous êtes en orbite stationnaire")
        else:
            print("\n\tLe vaisseau descend")

    def resultat(self):
        v = self.vaisseau.getVitesse()

        if v > 100:
            print("\nLe vaisseau s'est fracassé, il n'y a pas de survivant.")
        elif v > 30:
            print("\nLe vaisseau s'est posé brutalement, pas sûr que vous puissiez redécoller.")
        else:
            print("\nBravo, alunissage parffaitement réussi !") 
        print("\nGame over")
                    
if __name__ == "__main__":
    print("Alunissage")
    print("----------\n")

    jeu = Alunissage()

    while jeu.enVol():
        jeu.affichage()
        jeu.pilotage()
        jeu.simulation()

    jeu.resultat()
