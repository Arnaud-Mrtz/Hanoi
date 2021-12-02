# C'est les classes des joueurs
import pygame
# Définition des classes qui représentent les joueurs

class Base1(pygame.sprite.Sprite):
    def __init__(self, n):
        super().__init__()
        self.img = pygame.image.load('assets/Base.png')
        self.image = pygame.transform.scale(self.img, (300, (n+2)*55))
        self.rect = self.image.get_rect()
        self.rect.x = 265-((n+1)*55//2)
        self.rect.y = 540
        self.mask = pygame.mask.from_surface(self.image)

class Base2(pygame.sprite.Sprite):
    def __init__(self, n):
        super().__init__()
        self.img = pygame.image.load('assets/Base.png')
        self.image = pygame.transform.scale(self.img, (300, (n+2)*55))
        self.rect = self.image.get_rect()
        self.rect.x = 530-((n+1)*55//2)
        self.rect.y = 540
        self.mask = pygame.mask.from_surface(self.image)

class Base3(pygame.sprite.Sprite):
    def __init__(self, n):
        super().__init__()
        self.img = pygame.image.load('assets/Base.png')
        self.image = pygame.transform.scale(self.img, (300, (n+2)*55))
        self.rect = self.image.get_rect()
        self.rect.x = 795-((n+1)*55//2)
        self.rect.y = 540
        self.mask = pygame.mask.from_surface(self.image)