#! /usr/bin/python
# -*- coding: utf-8 -*-

class Module():

    def __init__(self):
        self.altitude  = 10000
        self.vitesse   =  1000
        self.carburant = 12000
        self.poussée   =     0

    def getAltitude(self):
        return self.altitude

    def getVitesse(self):
        return self.vitesse

    def getCarburant(self):
        return self.carburant

    def getPoussée(self):
        return self.poussée

    def setAltitude(self, altitude):
        self.altitude = altitude

    def monte(self, q):
        self.altitude += q

    def setVitesse(self, vitesse):
        self.vitesse = vitesse

    def setCarburant(self, carburant):
        self.carburant = carburant

    def setPoussée(self, poussée):
        self.poussée = poussée

class Alunissage():

    def __init__(self):
        self.étape    = 1
        self.heure    = 0
        self.vaisseau = Module()
        print("L'altitude du vaisseau en orbite est {}".format(self.vaisseau.getAltitude()))

    def enVol(self):
        pass

    def affichage(self):
        pass

    def pilotage(self):
        pass

    def simulation(self):
        pass
        
if __name__ == "__main__":
    print("Alunissage")
    print("----------\n")

    jeu = Alunissage()

    while jeu.enVol():
        jeu.affichage()
        jeu.pilotage()
        jeu.simulation()

