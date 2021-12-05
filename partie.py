                                # Classe qui définit le jeu
import pygame
from disks import Disks1, Disks2, Disks3, Disks4, Disks5, Disks6, Disks7, Disks8, Disks9, Disks10
from bases import Base1,Base2,Base3
class Partie():
    # liaison entre le main et les entités
    def __init__(self):
        super().__init__()
        self.base1 = Base1()
        self.base2= Base2()
        self.base3 = Base3()
        self.disks1 = Disks1()
        self.disks2 = Disks2()
        self.disks3 = Disks3()
        self.disks4 = Disks4()
        self.disks5 = Disks5()
        self.disks1 = Disks6()
        self.disks2 = Disks7()
        self.disks3 = Disks8()
        self.disks4 = Disks9()
        self.disks5 = Disks10()
        # Crétion d'un dico qui définit l'état des touche (True si elle est pressée, False quand la touche ne l'est plus)
        self.pressed = {}

    def deplacement(disk, de, a, nb_disk_de, nb_disk_a):
        self.disk.rect.move_ip(0, 55*(nb_disk+1)-540)
        self.disk.rect.move_ip(265*(a-de), 0)
        self.disk.rect.move_ip(0, 540-55*(nb_disk+1))

