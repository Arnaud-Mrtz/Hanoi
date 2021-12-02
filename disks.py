# C'est les classes des joueurs
import pygame
# Définition des classes qui représentent les joueurs

class Disk1(pygame.sprite.Sprite):
    def __init__(self, n):
        super().__init__()
        self.img = pygame.image.load('assets/disk_open_1.png')
        self.vitesse = 5
        self.image = pygame.transform.scale(self.img, (55, 55))
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 360
        self.mask = pygame.mask.from_surface(self.image)
    def up(self):
        self.rect.move_ip(0, -self.vitesse)
    def down(self):
        self.rect.move_ip(0, self.vitesse)


class Disk2(pygame.sprite.Sprite):
    def __init__(self, n):
        super().__init__()
        self.img = pygame.image.load('assets/disk_open_2.png')
        self.vitesse = 5
        self.image = pygame.transform.scale(self.img, (110, 55))
        self.rect = self.image.get_rect()
        self.rect.x = 1030
        self.rect.y = 360
        self.mask = pygame.mask.from_surface(self.image)
    def up(self):
        self.rect.move_ip(0, -self.vitesse)
    def down(self):
        self.rect.move_ip(0, self.vitesse)

class Disk3(pygame.sprite.Sprite):
    def __init__(self, n):
        super().__init__()
        self.img = pygame.image.load('assets/disk_open_3.png')
        self.vitesse = 5
        self.image = pygame.transform.scale(self.img, (165, 55))
        self.rect = self.image.get_rect()
        self.rect.x = 1030
        self.rect.y = 360
        self.mask = pygame.mask.from_surface(self.image)
    def up(self):
        self.rect.move_ip(0, -self.vitesse)
    def down(self):
        self.rect.move_ip(0, self.vitesse)

class Disk4(pygame.sprite.Sprite):
    def __init__(self, n):
        super().__init__()
        self.img = pygame.image.load('assets/disk_open_4.png')
        self.vitesse = 5
        self.image = pygame.transform.scale(self.img, (220, 55))
        self.rect = self.image.get_rect()
        self.rect.x = 1030
        self.rect.y = 360
        self.mask = pygame.mask.from_surface(self.image)
    def up(self):
        self.rect.move_ip(0, -self.vitesse)
    def down(self):
        self.rect.move_ip(0, self.vitesse)

class Disk5(pygame.sprite.Sprite):
    def __init__(self, n):
        super().__init__()
        self.img = pygame.image.load('assets/disk_open_5.png')
        self.image = pygame.transform.scale(self.img, (275, 55))
        self.rect = self.image.get_rect()
        self.rect.x = 1030
        self.rect.y = 360
        self.mask = pygame.mask.from_surface(self.image)
    def up(self):
        self.rect.move_ip(0, -self.vitesse)
    def down(self):
        self.rect.move_ip(0, self.vitesse)

class Disk6(pygame.sprite.Sprite):
    def __init__(self, n):
        super().__init__()
        self.img = pygame.image.load('assets/disk_open_1.png')
        self.vitesse = 5
        self.image = pygame.transform.scale(self.img, (330, 55))
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 360
        self.mask = pygame.mask.from_surface(self.image)
    def up(self):
        self.rect.move_ip(0, -self.vitesse)
    def down(self):
        self.rect.move_ip(0, self.vitesse)


class Disk7(pygame.sprite.Sprite):
    def __init__(self, n):
        super().__init__()
        self.img = pygame.image.load('assets/disk_open_2.png')
        self.vitesse = 5
        self.image = pygame.transform.scale(self.img, (385, 55))
        self.rect = self.image.get_rect()
        self.rect.x = 1030
        self.rect.y = 360
        self.mask = pygame.mask.from_surface(self.image)
    def up(self):
        self.rect.move_ip(0, -self.vitesse)
    def down(self):
        self.rect.move_ip(0, self.vitesse)

class Disk8(pygame.sprite.Sprite):
    def __init__(self, n):
        super().__init__()
        self.img = pygame.image.load('assets/disk_open_3.png')
        self.vitesse = 5
        self.image = pygame.transform.scale(self.img, (440, 55))
        self.rect = self.image.get_rect()
        self.rect.x = 1030
        self.rect.y = 360
        self.mask = pygame.mask.from_surface(self.image)
    def up(self):
        self.rect.move_ip(0, -self.vitesse)
    def down(self):
        self.rect.move_ip(0, self.vitesse)

class Disk9(pygame.sprite.Sprite):
    def __init__(self, n):
        super().__init__()
        self.img = pygame.image.load('assets/disk_open_4.png')
        self.vitesse = 5
        self.image = pygame.transform.scale(self.img, (495, 55))
        self.rect = self.image.get_rect()
        self.rect.x = 1030
        self.rect.y = 360
        self.mask = pygame.mask.from_surface(self.image)
    def up(self):
        self.rect.move_ip(0, -self.vitesse)
    def down(self):
        self.rect.move_ip(0, self.vitesse)

class Disk10(pygame.sprite.Sprite):
    def __init__(self, n):
        super().__init__()
        self.img = pygame.image.load('assets/disk_open_5.png')
        self.image = pygame.transform.scale(self.img, (1050, 55))
        self.rect = self.image.get_rect()
        self.rect.x = 1030
        self.rect.y = 360
        self.mask = pygame.mask.from_surface(self.image)
    def up(self):
        self.rect.move_ip(0, -self.vitesse)
    def down(self):
        self.rect.move_ip(0, self.vitesse)