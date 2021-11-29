# Classe qui d�finit le jeu
import pygame
from disks import Disks1, Disks2, Disks3, Disks4, Disks5
from bases import Base1,Base2,Base3
class Partie():
    # liaison entre le main et les entités
    def __init__(self):
        super().__init__()
        self.ball = Ball()
        self.disks1 = Disks1()
        self.disks2 = Disks2()
        # Cr�tion d'un dico qui d�finit l'état des touche (True si elle est press�e, False si la touche ne l'est plus)
        self.pressed = {}
        self.ply = None
        self.score = {}
        
                

    def ball_mouv(self):
        mouv = True
        self.depx = self.vitesse
        self.depy = 0
        self.ply = 1
        if mouv == True:
            self.check_victory()
            self.rotate()
            self.rect.move(self.depx, self.depy)
            if self.check_collision():
                if self.ply == 1:
                    self.depx = self.vitesse
                    if  self.rect.y < self.disks1.rect.y + 30:
                        self.depy = self.vitesse/2
                    elif  self.rect.y > self.disks1.rect.y + 70:
                        self.depy = -self.vitesse/2
                    else:
                        self.depy = 0
                else:
                    self.vitesse += 1