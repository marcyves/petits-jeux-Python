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
        if altitude<0:
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
        return (self.poussée//2 + carburant)//2

    def setPoussée(self, poussée):
        self.poussée = poussée
    
    def setPousséeMax(self, poussée):
        self.pousséeMax = poussée

class Alunissage():

    def __init__(self, niveau, niveaux):
        self.étape       =   1
        self.heure       =   0
        self.gravitation = 100

        for n in niveaux:
            if niveaux[n][0] == niveau:
                altitude   = niveaux[n][1]
                vitesse    = niveaux[n][2]
                carburant  = niveaux[n][3]
                poussée    = niveaux[n][4]
                pousséeMax = niveaux[n][5]

        self.vaisseau = Module(altitude, vitesse, carburant, poussée, pousséeMax)
        print("L'altitude du vaisseau en orbite est {}".format(self.vaisseau.getAltitude()))

    def enVol(self):
        if self.vaisseau.getAltitude()>0:
            return True
        else:
            return False

    def affichage(self, msg):
        print("\n\t+------------------------------------+")
        print("\t| - - - - - - - - {:>2} - - - - - - - - |".format(self.étape))
        print("\t+------------------------------------+")
        if self.vaisseau.getCarburant() <= 0:
            print("\t| {:^34} |".format("Vous êtes à court de carburant !"))
            print("\t+------------------------------------+")
        print("\t| {:^34} |".format(msg))
        print("\t+------------------------------------+")
        print("\t| Altitude {:>5} m   Carburant {:>5} |".format(self.vaisseau.getAltitude(), self.vaisseau.getCarburant()))
        print("\t| Vitesse  {:>5} m/s Poussée   {:>5} |".format(self.vaisseau.getVitesse(), self.vaisseau.getPoussée()))
        print("\t+------------------------------------+")

    def pilotage(self):
        carburant = -1
        while(carburant<0 or carburant>self.vaisseau.getPousséeMax()):
            try:
                carburant = int(input("Combien bruler de carburant (max={}) ==> ".format(self.vaisseau.getPousséeMax())))
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
            print("\nBravo, alunissage parffaitement réussi !") 
        print("\nGame over")
                    
if __name__ == "__main__":
    print("\n\n----------")
    print("Alunissage")
    print("----------\n")

    niveaux = { 'Facile':[
        1,          # numéro du niveau
        5000,       # altitude de départ
        1000,       # vitesse initiale
        4000,       # quantité de carburant
        0,          # poussée initiale
        500         # quantité maximum de carburant brulée dans 1 tour
        ],
                'Basse altitude':[2, 2000,500,2000,0,500],
                'Moteur peu puissant':[3, 2000,1000,2000,0,200],
                'Manque de carburant':[4, 2000,1000,500,0,200],
                }
    print("Choisssez votre niveau dans la liste suivante\n")
    for niveau in niveaux:
        print("\t{} - {}".format(niveaux[niveau][0], niveau))

    niveau = -1
    while(niveau<0 or niveau>len(niveaux)):
        try:
            niveau = int(input("\nQuel niveau voulez-vous essayer ? ==> "))
        except ValueError:
            niveau = 1

    jeu = Alunissage(niveau, niveaux)

    message = "C'est parti"
    while jeu.enVol():
        jeu.affichage(message)
        jeu.pilotage()
        message = jeu.simulation()

    jeu.affichage("Game Over")
    jeu.resultat()

