# C'est la classe de la balle
import pygame
# Définition de la classe qui gère la balle
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.vitesse = 5
        self.image = pygame.image.load('assets/ball.gif')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = pygame.display.get_surface().get_width()/2
        self.rect.y = pygame.display.get_surface().get_height()/2
        self.origin_image = self.image
        self.angle = 0


    def rotate(self):
        self.angle +=8
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)