import pytmx
import os
from Case import Case
import pygame

class PlateauDeJeu:

    # lire une fois le fichier ==> créer les objets qui découlent de ce fichier dans plateau de jeu

    def __init__(self,fichier):
        if os.path.isfile(fichier):
            self.__map = fichier
        else:
            self.__map = None
        

    def getMap(self) -> str:
        return self.__map

    def generatePlateau(self) -> None:
        tmxdata = pytmx.util_pygame.load_pygame(self.__map)
        self.__width = tmxdata.width
        self.__height = tmxdata.height
        self.__tilewidth = tmxdata.tilewidth
        self.__tileheight = tmxdata.tileheight
        
        self.__plateau = []
        images = []
        gid = []
        
        for i in range(self.__width):
            self.__plateau.append([])
            images.append([])
            gid.append([])
            for j in range(self.__height):
                self.__plateau[i].append(None)
                images[i].append(None)
                gid[i].append(None)

        for layer in tmxdata.layers:
            for x, y, image in layer.tiles():
                images[x][y] = image
                gid[x][y] = tmxdata.tiledgidmap[layer.data[x][y]]
        
        for i in range(self.__width):
            for j in range(self.__height):
                self.__plateau[i][j] = Case(images[i][j], gid[i][j])
                
        self.__tileheight *= 2
        self.__tilewidth *= 2
                
  
    def getCase(self, coord:tuple) -> Case :
        return None

    def render(self, window):
        for i in range(self.__width):
            mod = 0
            if i%2 == 1:
                mod = self.__tilewidth/2
            else:
                mod = 0
            for j in range(self.__height):
                window.blit(pygame.transform.scale(self.__plateau[j][i].getImage(), (self.__tilewidth, self.__tileheight)), (j*self.__tilewidth + mod, i*self.__tileheight*0.78125))
