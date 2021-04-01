# from Personnage import Personnage
import pygame
from math import floor

class EquipeDePersonnages:
    def __init__(self,personnages):
        self.__coord = (0,0)
        self.__estVivante : bool = True
        self.__personnages : list = personnages

    def __len__(self) -> int:
        return len(self.__personnages)

    def deplacement(self, coord) -> tuple:
        self.__coord = coord
    
    def render(self, window, dimmensions) -> None :
        longueur = len(self)
        
        if (longueur == 1):
            pygame.draw.circle(window, (255,0,0), ((self.__coord[0] * dimmensions[0]) + floor(dimmensions[0]/2), (self.__coord[1] * dimmensions[1]) + floor(dimmensions[1]/2)), 5, 4)
        elif (longueur == 2):
            pygame.draw.circle(window, (255,0,0), ((self.__coord[0] * dimmensions[0]) + floor(dimmensions[0]/2) - 10, (self.__coord[1] * dimmensions[1]) + floor(dimmensions[1]/2)), 5, 4)
            pygame.draw.circle(window, (0,255,0), ((self.__coord[0] * dimmensions[0]) + floor(dimmensions[0]/2) + 10, (self.__coord[1] * dimmensions[1]) + floor(dimmensions[1]/2)), 5, 4)
        elif (longueur == 3):
            pygame.draw.circle(window, (255,0,0), ((self.__coord[0] * dimmensions[0]) + floor(dimmensions[0]/2) - 10, (self.__coord[1] * dimmensions[1]) + floor(dimmensions[1]/2) - 7), 5, 4)
            pygame.draw.circle(window, (0,255,0), ((self.__coord[0] * dimmensions[0]) + floor(dimmensions[0]/2) + 10, (self.__coord[1] * dimmensions[1]) + floor(dimmensions[1]/2) - 7), 5, 4)
            pygame.draw.circle(window, (0,0,255), ((self.__coord[0] * dimmensions[0]) + floor(dimmensions[0]/2), (self.__coord[1] * dimmensions[1]) + floor(dimmensions[1]/2) + 7), 5, 4)
        else:
            print("wtf tu as mis combiens de personnes dans ton Equipe mec !!")
        