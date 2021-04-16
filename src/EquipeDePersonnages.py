from Personnage import Personnage
import pygame
from math import floor


class EquipeDePersonnages:
    def __init__(self, personnages):
        self._coord = (0, 0)
        self._estVivante: bool = True
        self._personnages: list = personnages

    def __len__(self) -> int:
        return len(self.__personnages)

    def getPersonnages(self) -> list[Personnage]:
        return self._personnages

    def getVivante(self) -> bool:
        return self._estVivante

    def __str__(self) -> none:
        for i in range(len(self._personnages)):
            self._personnages[i].__str__()


    def deplacement(self, coord) -> tuple:
        self._coord = coord

    def render(self, window, dimmensions) -> None:
        longueur = len(self)
        mod = 0
        if self._coord[1] % 2 == 1:
            mod = floor(dimmensions[0] / 2)
        else:
            mod = 0

        coordPixel = ((self._coord[0] * dimmensions[0]) + floor(dimmensions[0] / 2) + mod,
                      floor((self._coord[1] * dimmensions[1]) * 0.75 + floor(dimmensions[1] / 2)))

        if longueur == 1:
            pygame.draw.circle(window, (255, 0, 0), coordPixel, 5, 4)
        elif longueur == 2:
            pygame.draw.circle(window, (255, 0, 0), (coordPixel[0] - 10, coordPixel[1]), 5, 4)
            pygame.draw.circle(window, (0, 255, 0), (coordPixel[0] + 10, coordPixel[1]), 5, 4)
        elif longueur == 3:
            pygame.draw.circle(window, (255, 0, 0), (coordPixel[0] - 10, coordPixel[1] - 7), 5, 4)
            pygame.draw.circle(window, (0, 255, 0), (coordPixel[0] + 10, coordPixel[1] - 7), 5, 4)
            pygame.draw.circle(window, (0, 0, 255), (coordPixel[0], coordPixel[1] + 7), 5, 4)
        else:
            print("wtf tu as mis combiens de personnes dans ton Equipe mec !!")
