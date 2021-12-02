# C'est les classes des joueurs
import pygame
# Définition des classes qui représentent les joueurs

class Cursor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img = pygame.image.load('assets/cursor.png')
        self.image = pygame.transform.scale(self.img, (300, 350))
        self.rect = self.image.get_rect()
        self.rect.x = 265
        self.rect.y = 600
        self.mask = pygame.mask.from_surface(self.image)
    def left(self):
        self.rect.move_ip(-265, 0) 
    def right(self):
        self.rect.move_ip(265, 0) 
