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

# Boucle du jeu

while True:
    # Insertion du fond d'écran 
    screen.blit(background, (0, 0))

    # Affichage des entités
        # Affichage des Bases
    screen.blit(partie.base1.image, partie.player1.rect)
    screen.blit(partie.base1.image, partie.player1.rect)
    screen.blit(partie.player1.image, partie.player1.rect)

    screen.blit(partie.player1.image, partie.player1.rect)
    screen.blit(partie.player2.image, partie.player2.rect)
    screen.blit(partie.player1.image, partie.player1.rect)
    screen.blit(partie.player2.image, partie.player2.rect)

    continuer = False
    for dem in pygame.event.get():
        if dem.type == pygame.KEYDOWN:
            if dem.key == pygame.K_SPACE:
                # Etat du du jeu (True s'il est en execution)
                continuer = True
    while continuer:
            # Definir si les joueurs veulent se déplacer vers le haut ou le bas
            if partie.pressed.get(pygame.K_a) and partie.player1.rect.top > 20:
                partie.player1.up()
            elif partie.pressed.get(pygame.K_q) and partie.player1.rect.bottom < screen.get_width() - 20:
                partie.player1.down()
            elif partie.pressed.get(pygame.K_UP) and partie.player1.rect.top > 20:
                partie.player2.up()
            elif partie.pressed.get(pygame.K_DOWN) and partie.player2.rect.bottom < screen.get_width() - 20:
                partie.player2.down()
            # Update de la fenêtre
            pygame.display.flip()
            partie.ball_mouv()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    break
                    pygame.quit()
                    print("Arrêt du jeu.")
                # Detecter si le joueur appuie ou non sur une touche via le dico
                elif event.type == pygame.KEYDOWN:
                    partie.pressed[event.key] = True
                    if event.key == pygame.K_SPACE:
                        partie.ball_mouv()
                elif event.type == pygame.KEYUP:
                    partie.pressed[event.key] = False
            print(partie.pressed)
            for nb in score.values():
                if nb < 7:
                    print(score)
                    break
                else:
                    print("Le joueur {} a gagné!".format(ply))
                    continuer = False
                    pygame.quit()
    else:
        print("appuyer sur la touche espace pour jouer.")