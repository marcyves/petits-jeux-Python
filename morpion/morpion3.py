#! /usr/bin/python

class Morpion:

    def __init__(self):
        self.tableau  = ["", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.pion_joueur = ""
        self.pion_ordi   = ""
        self.qui_joue    = ""
        self.actif       = True

    def choix_pion(self):
        print("\n\tPetit jeu de Morpion")
        print("\t--------------------\n\n")

        print("Choissisez votre pion pour décider qui commence (O)")

        while (self.pion_joueur != "O" and self.pion_joueur != "X"):
            self.pion_joueur = input("Est-ce que vous jouez O ou X ? ==> ").upper()

        if self.pion_joueur == "O":
            self.pion_ordi = "X"
            self.qui_joue  = "joueur" 
            print("C'est vous qui commencez")
        else:
            self.pion_ordi = "O"
            self.qui_joue  = "ordi"
            print("C'est moi qui commence")

    def affiche_jeu(self):
        print("\t " + self.tableau[1] + " | " + self.tableau[2] + " | " + self.tableau[3])
        print("\t---+---+---")
        print("\t " + self.tableau[4] + " | " + self.tableau[5] + " | " + self.tableau[6])
        print("\t---+---+---")
        print("\t " + self.tableau[7] + " | " + self.tableau[8] + " | " + self.tableau[9])
        print("\n")

    def jeu_joueur(self):
        coup_joueur = 0
        while (coup_joueur < 1 or coup_joueur > 9):
            coup_joueur = int(input("\nOù est-ce que vous placez votre pion ? ==> "))
            if self.tableau[coup_joueur] != str(coup_joueur):
                print("Coup invalide, la case est déjà occupée")
                coup_joueur = 0

        self.tableau[coup_joueur] = self.pion_joueur

    def jeu_ordi(self):
        print("À moi de jouer")
        coup_ordi = self.cherche_position_gagnante()

        if coup_ordi == 0:
            if self.tableau[5] == "5":
                coup_ordi = 5
            else:
                coup_ordi = self.cherche_solution()

        print("Je joue en position {}".format(coup_ordi))
        self.tableau[coup_ordi] = self.pion_ordi

    def cherche_position_gagnante(self):
        return 0

    def cherche_solution(self):
        return 0
        
    def joueur(self):
        if self.qui_joue == "ordi":
            return False
        else:
            return True
    
    def en_cours(self):
        return self.actif

    def terminée(self):
        if self.joueur():
            pion = self.pion_joueur
        else:
            pion = self.pion_ordi

        if ((self.tableau[1] == pion and self.tableau[2] == pion and self.tableau[3] == pion) or
            (self.tableau[4] == pion and self.tableau[5] == pion and self.tableau[6] == pion) or
            (self.tableau[7] == pion and self.tableau[8] == pion and self.tableau[9] == pion) or
            (self.tableau[1] == pion and self.tableau[4] == pion and self.tableau[7] == pion) or
            (self.tableau[2] == pion and self.tableau[5] == pion and self.tableau[8] == pion) or
            (self.tableau[3] == pion and self.tableau[6] == pion and self.tableau[9] == pion) or
            (self.tableau[1] == pion and self.tableau[5] == pion and self.tableau[9] == pion) or
            (self.tableau[7] == pion and self.tableau[5] == pion and self.tableau[3] == pion)):
            if self.joueur():
                print("Bravo, vous avez gagné !")
            else:
                print("J'ai gagné !")
            self.actif = False

    def a_toi(self):
            if self.joueur():
                self.qui_joue = "ordi"
            else:
                self.qui_joue = "joueur"

if __name__ == "__main__":

    partie = Morpion()

    partie.choix_pion()

    while partie.en_cours():
        if partie.joueur() :
            partie.affiche_jeu()
            partie.jeu_joueur()
            partie.terminée()
            partie.a_toi()
        else:
            partie.jeu_ordi()
            partie.terminée()
            partie.a_toi()

        partie.affiche_jeu()

    print("Au revoir")