# C'est les classes des joueurs
import pygame
# Définition des classes qui représentent les joueurs

class Base1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img = pygame.image.load('assets/Base.png')
        self.image = pygame.transform.scale(self.img, (40, 100))
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 360
        self.mask = pygame.mask.from_surface(self.image)


class Base2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img = pygame.image.load('assets/Base.png')
        self.image = pygame.transform.scale(self.img, (40, 100))
        self.rect = self.image.get_rect()
        self.rect.x = 1030
        self.rect.y = 360
        self.mask = pygame.mask.from_surface(self.image)

class Base3(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img = pygame.image.load('assets/Base.png')
        self.image = pygame.transform.scale(self.img, (40, 100))
        self.rect = self.image.get_rect()
        self.rect.x = 1030
        self.rect.y = 360
        self.mask = pygame.mask.from_surface(self.image)