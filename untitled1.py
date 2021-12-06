class Pythagore:
    def __init__(self, longueurs):
        self.A=max(longueurs)
        longueurs.remove(max(longueurs))
        self.B=longueurs[0]
        self.C=longueurs[1]
        self.check(self.A, self.B, self.C)
    def check(self, A, B, C):
        if self.A**2 == self.B**2 + self.C**2:
            print("C'est un triangle rectangle")
        else:
            print("Ce n'est pas un triangle rectangle")
cotés = []
cotés.append(int(input("1re longueur : ")))
cotés.append(int(input("2e longueur : ")))
cotés.append(int(input("3e longueur : ")))
fonction = Pythagore(cotés)