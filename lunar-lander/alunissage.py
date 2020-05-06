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

        
if __name__ == "__main__":
    print("Alunissage")
    print("----------\n")

    vaisseau = Module()
    print("L'altitude du vaisseau est {}".format(vaisseau.getAltitude()))

