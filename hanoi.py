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




# Insertion du fond d'écran 
screen.blit(background, (0, 0))

# # Affichage des entités
#     # Affichage des Bases
# screen.blit(partie.base1.image, partie.base1.rect)
# screen.blit(partie.base2.image, partie.base2.rect)
# screen.blit(partie.base3.image, partie.base3.rect)

     # Affichage des Disques
# screen.blit(partie.disk1.image, partie.disk1.rect)
# Fonction résolution automatique
def resolution(n, de , a, par):

    disk = globals()[de[len(de)-1]]
    if de == A:
        base_de = 1
    elif de == B:
        base_de = 2
    elif de == C:
        base_de = 3
    if a == A:
        base_a = 1
    elif a == B:
        base_a = 2
    elif a == C:
        base_a = 3
    if n>0:
        resolution(n-1,de, par, a)
        #système de pile (ce qu'on dépile à de, on l'empile à a)
        a.append(de[len(de)-1])
        partie.deplacement(disk, base_de, base_a, len(de), len(de))
        de.pop()

        print("""

            Etape suivante :
        """)
        print("Base 1"+str(A))
        print("Base 2"+str(B))
        print("Base 3"+str(C))
        
        resolution(n-1, par, a, de)
Disks=["disks10","disks9","disks8","disks7","disks6","disks5","disks4","disks3","disks2","disks1"]
A=[]
B=[]
C=[]
print("""
Tours de Hanoi
Voici les la liste des déplacements pour faire passer les disques de la tour A vers la tour C
""")


# Affichage des entités
def creation(n):
    # Affichage des Disques
    for j in range(n):
        exec('screen.blit(partie.disk'+str(j)+'.image, partie.disk'+str(j)+'.rect)')
    # Affichage des Bases
    for k in range(3):
        exec('screen.blit(partie.base'+str(k)+'.image, partie.base'+str(k)+'.rect)')


n = int(input("Nombre de disques (de 1 à 10) : "))
res = input("Résoudre automatiquement? : ")
if res == "oui":
    for i in range(n):
        A.append(Disks[i+(len(Disks)-n)])
    print(A)
    resolution(n,A,C,B)
    print("Bon jeu.")


# # Definir si les joueurs veulent se déplacer vers le haut ou le bas
# if partie.pressed.get(pygame.K_LEFT) and partie.player1.rect.top > 20:
#     partie.player1.up()
# elif partie.pressed.get(pygame.K_RIGHT) and partie.player1.rect.bottom < screen.get_width() - 20:
#     partie.player1.down()

# # Update de la fenêtre
# pygame.display.flip()
# partie.ball_mouv()
# for event in pygame.event.get():
#     if event.type == pygame.QUIT:
#         break
#         pygame.quit()
#         print("Arrêt du jeu.")
#     # Detecter si le joueur appuie ou non sur une touche via le dico
#     elif event.type == pygame.KEYDOWN:
#         partie.pressed[event.key] = True
#         if event.key == pygame.K_SPACE:
#             partie.ball_mouv()
#     elif event.type == pygame.KEYUP:
#         partie.pressed[event.key] = False
# print(partie.pressed)
# pygame.quit()