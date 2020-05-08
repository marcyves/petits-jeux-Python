#! /usr/bin/python
# -*- coding: utf-8 -*-

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
        self.vaisseau = Module(5000, 1000, 6000, 200, 500)
        print("L'altitude du vaisseau en orbite est {}".format(self.vaisseau.getAltitude()))

    def enVol(self):
        if self.vaisseau.getAltitude()>0:
            return True
        else:
            return False

    def affichage(self, message):
        print("\n\t+------------------------------------+")
        print("\t| - - - - - - - - {:>2} - - - - - - - - |".format(self.étape))
        print("\t+------------------------------------+")
        if self.vaisseau.getCarburant() <= 0:
            print("\t| {:^34} |".format("Vous êtes à court de carburant !"))
            print("\t+------------------------------------+")
        print("\t| {:^34} |".format(message))
        print("\t+------------------------------------+")
        print("\t| Altitude {:>5} m   Carburant {:>5} |".format(self.vaisseau.getAltitude(), self.vaisseau.getCarburant()))
        print("\t| Vitesse  {:>5} m/s Poussée   {:>5} |".format(self.vaisseau.getVitesse(), self.vaisseau.getPoussée()))
        print("\t+------------------------------------+")

    def pilotage(self):
        carburant = -1
        while(carburant<0 or carburant>self.vaisseau.getPousséeMax()):
            try:
                carburant = int(input("\nCombien bruler de carburant (max={:<3}) ==> ".format(self.vaisseau.getPousséeMax())))
            except ValueError:
               carburant = 0

        poussée = self.vaisseau.bruleCarburant(carburant)
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
                    
if __name__ == "__main__":
    print("Alunissage")
    print("----------\n")

    jeu = Alunissage()

    message = "C'est parti !"
    while jeu.enVol():
        jeu.affichage(message)
        jeu.pilotage()
        message = jeu.simulation()

    jeu.affichage("Game Over")
    jeu.resultat()

