import random
class Personnage:
    def __init__(self, nom, nbreDeVie):
        self.nom = nom
        self.vies = nbreDeVie

    def donneEtat(self, nom, vies):
        print(str(self.nom)+" a "+str(self.vies)+" vies")

    def PerdVie(self, nom, vies, dgt):
        self.vies -= dgt
        self.donneEtat(nom, vies)

    def BoirePotion(self, nom, vies, gain):
        self.vies += gain
        self.donneEtat(nom, vies)


Gollumont = Personnage("Gollumont",150)
Bilbo = Personnage("Bilbo",200)

Bilbo.donneEtat("Bilbo",200)
Gollumont.PerdVie("Gollumont",150, random.randint(1,5)*10)
Gollumont.PerdVie("Gollumont",150, random.randint(1,5)*10)
Gollumont.PerdVie("Gollumont",150, random.randint(1,5)*10)
Gollumont.BoirePotion("Gollumont",150 , 120)
