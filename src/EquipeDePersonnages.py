# from Personnage import Personnage
import pygame

class EquipeDePersonnages:
    def __init__(self,personnages):
        self.__coord = (0,0)
        self.__estVivante = True
        self.__personnages = personnages

    def __len__(self):
        return len(self.__personnages)

    def deplacement(self, coord):
        self.__coord = coord
    
    def render(self):
        longueur = len(self)
        if (longueur == 1):
            pygame.draw.circle(screen, (255,0,0), self.coord * 64, 5, 3)
        elif (longueur == 2):
            pygame.draw.circle(screen, (255,0,0), (self.coord[0] * 64 - 10, self.coord[0] * 64), 5, 3)
            pygame.draw.circle(screen, (0,255,0), (self.coord[0] * 64 + 10, self.coord[0] * 64), 5, 3)
        elif (longueur == 3):
            pygame.draw.circle(screen, (255,0,0), (self.coord[0] * 64 - 10, self.coord[1] * 64), 5, 3)
            pygame.draw.circle(screen, (0,255,0), (self.coord[0] * 64 + 10, self.coord[1] * 64), 5, 3)
            pygame.draw.circle(screen, (0,0,255), (self.coord[0] * 64, self.coord[1] * 64), 5, 3)
        else:
            print("wtf tu as mis combiens de personnes dans ton Equipe mec !!")
        