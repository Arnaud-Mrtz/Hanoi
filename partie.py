# Classe qui définit le jeu
import pygame
from players import Player1
from players import Player2
from ball import Ball
class Partie():
    # liaison entre le main et les entitÃ©s
    def __init__(self):
        super().__init__()
        self.ball = Ball()
        self.player1 = Player1()
        self.player2 = Player2()
        # Crétion d'un dico qui définit l'Ã©tat des touche (True si elle est pressée, False si la touche ne l'est plus)
        self.pressed = {}
        self.ply = None
        self.score = {}
        
    def check_collision(self):
        if self.ball.rect.midleft <= self.player1.rect.right and self.ball.rect.midleft >= self.player1.rect.left:
            if self.ball.rect.centery >= self.player1.rect.top and self.ball.rect.centery >= self.player1.rect.bottom:
                self.ply = 1
                return True
        if self.ball.rect.midleft >= self.player2.rect.right and self.ball.rect.midleft <= self.player2.rect.left:
            if self.ball.rect.centery >= self.player2.rect.top and self.ball.rect.centery <= self.player2.rect.bottom:
                self.ply = 2
                return True
                
            
    def check_victory(self):
        xcor = self.ball.rect.x
        if xcor < 20 or xcor >= pygame.display.get_surface().get_width() - 20:
            if self.score.has_key("Joueur : {}".format(self.ply)):
                self.score[("Joueur : {}".format(self.ply))] += 1
                mouv = False
                return True
            else:
                self.score[("Joueur : {}".format(self.ply))] = 1
                mouv = False
                return True


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
                    if  self.rect.y < self.player1.rect.y + 30:
                        self.depy = self.vitesse/2
                    elif  self.rect.y > self.player1.rect.y + 70:
                        self.depy = -self.vitesse/2
                    else:
                        self.depy = 0
                else:
                    self.vitesse += 1