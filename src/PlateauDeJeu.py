import pytmx
import xml.etree.ElementTree
import os
from Case import Case
import pygame
import math


class PlateauDeJeu:

    # lire une fois le fichier ==> créer les objets qui découlent de ce fichier dans plateau de jeu

    def __init__(self, fichier):
        if os.path.isfile(fichier):
            self.__map = fichier
            self.generatePlateau()
        else:
            raise FileNotFoundError("Le fichier de map n'existe pas ...")

    def getMap(self) -> str:
        return self.__map

    def generatePlateau(self) -> None:
        try:
            tmxdata = pytmx.util_pygame.load_pygame(self.__map)
        except xml.etree.ElementTree.ParseError:
            raise FileExistsError("Le fichier n'a pas le bon format et n'a pas pu être chargé ...")
        else:
            print("Chargement de la map réussi !")
        self.__nblayers = len(tmxdata.layers)
        self.__width = tmxdata.width
        self.__height = tmxdata.height
        self.__tilewidth = tmxdata.tilewidth
        self.__tileheight = tmxdata.tileheight

        self.__plateau = []
        images = []
        typeCase = []

        for l in range(self.__nblayers):
            self.__plateau.append([])
            images.append([])
            typeCase.append([])
            for i in range(self.__width):
                self.__plateau[l].append([])
                images[l].append([])
                typeCase[l].append([])
                for j in range(self.__height):
                    self.__plateau[l][i].append(None)
                    images[l][i].append(0)
                    typeCase[l][i].append(0)

        l = 0
        for layer in tmxdata.layers:
            for x, y, image in layer.tiles():
                images[l][x][y] = image
                try:
                    typeCase[l][x][y] = tmxdata.get_tile_properties_by_gid(layer.data[x][y])["type"]
                except KeyError:
                    print(x, y, "il n'y pas de type de case sur cette case ...")

            l += 1

        for l in range(self.__nblayers):
            for i in range(self.__width):
                for j in range(self.__height):
                    self.__plateau[l][i][j] = Case(images[l][i][j], typeCase[l][i][j])

        self.__tileheight /= 2
        self.__tilewidth /= 2
        self.__tileheight = math.floor(self.__tileheight)
        self.__tilewidth = math.floor(self.__tilewidth)

    def getCase(self, coord: tuple) -> Case:
        return self.__plateau[0][coord[1]][coord[0]]

    def getTileheight(self) -> int:
        return self.__tileheight

    def getTilewidth(self) -> int:
        return self.__tilewidth

    def getHeight(self) -> int:
        return self.__height

    def getWidth(self) -> int:
        return self.__width

    def isInTheMap(self, coord: tuple) -> bool:
        return (coord[0] >= 0) & (coord[0] < self.__height) & (coord[1] >= 0) & (coord[1] < self.__width)

    def render(self, window):
        for l in range(self.__nblayers):
            for i in range(self.__width):
                mod = 0
                if i % 2 == 1:
                    mod = self.__tilewidth / 2
                else:
                    mod = 0
                for j in range(self.__height):
                    window.blit(pygame.transform.scale(self.__plateau[l][j][i].getImage(), (self.__tilewidth, self.__tileheight)), (j * self.__tilewidth + mod, i * self.__tileheight * 0.75))
