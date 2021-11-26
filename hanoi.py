# MARTINEZ Arnaud
# Importation de pygame et initialisation du module
import pygame
from partie import Partie
pygame.init()


# Création de la fenêtre ( titre et dimentions de la fenêtre)
pygame.display.set_caption("Hanoi!")
screen = pygame.display.set_mode((1080, 720))


# Importation d'une image qui sera la fond d'écran dans la variable background
background = pygame.image.load('assets/background.jpg')

# Lien pour entrer dans la class Partie du fichier partie importé ci-dessus
partie = Partie()
