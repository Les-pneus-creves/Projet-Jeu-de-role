from EquipeDePersonnages import EquipeDePersonnages
import Evenement
import math
from PlateauDeJeu import PlateauDeJeu
import pygame

class Expedition:

    def __init__(self, equipe, plateau):
        self.__temps: int = 1             #Numéro du tour de l'expédition en cour
        self.__equipe: EquipeDePersonnages = EquipeDePersonnages([1])          #Equipe de personnage joueur du joueur
        self.__eventEnCours: Evenement = None      #Even ement actuellement en cours
        self.__plateau: PlateauDeJeu = plateau     #Plateau sur lequel l'éxpedition se déroule

    # lecture des evenements
    def on_event(self, event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:    #Lorsque je clic gauche sur une unite et que j'en ai pas de selectionnée

            xInMap = int(event.pos[0]) # Enregistre la coordonnée y de l'event
            yInMap = int(event.pos[1]) # Enregistre la coordonnée y de l'event

            print("clic", xInMap, " ", yInMap)
            print(self.pointToCoord((xInMap,yInMap)))
           
    #Calcul des mises à jours
    def on_loop(self) -> None:
        pass
    
    #Calcul des affichages
    def on_render(self, window) -> None:
        self.__plateau.render(window)
        self.__equipe.render(window, (self.__plateau.getTilewidth(), self.__plateau.getTileheight()))
        for i in range(16):
            for y in range(16):
                pygame.draw.rect(window, (255,0,0), (i*self.__plateau.getTilewidth(),y*self.__plateau.getTileheight(),self.__plateau.getTilewidth(),self.__plateau.getTileheight()), 1)


    #Méthode permettant de sélectionner aléatoirement (ou non?) un plateau
    def selectPlateau(self)  -> None:
        pass


    #Méthode lançant un événement précis
    def lancerEvenement(self,evenement) -> None:
        pass


    #Méthode retournant true ou false selon si des coordonnées (En pixel ou en case/hexagone??) sont effectivement dans la map
    def estDansLaMap(self,coord) -> bool:
        pass

    
    def pixel_to_hex(self,coord: tuple):
        q = (math.sqrt(3)/3 * coord[0] - 1/3 * coord[1]) / 64   #q: colonne
        r = (2/3 * coord[1]) / 64                               #r: row    
        return self.hex_round((q,r))

    def hex_round(self, coord: tuple):
        return self.cube_to_axial(self.cube_round(self.axial_to_cube(coord)))

    def cube_round(self, coordCube: tuple):
        rx = round(coordCube[0])
        ry = round(coordCube[1])
        rz = round(coordCube[2])

        x_diff = abs(rx - coordCube[0])
        y_diff = abs(ry - coordCube[1])
        z_diff = abs(rz - coordCube[2])

        if x_diff > y_diff and x_diff > z_diff:
            rx = -ry-rz
        elif y_diff > z_diff:
            ry = -rx-rz
        else:
            rz = -rx-ry

        return(rx,ry,rz)

    def cube_to_axial(self, coordCube: tuple):
        q = coordCube[0]
        r = coordCube[2]
        return (q,r)
        
    def axial_to_cube(self,coord: tuple):
        x = coord[0]
        z = coord[1]
        y = -x-z
        return (x,y,z) #des coordCube en gros
                                                               
    def  pointToCoord(self, coord: tuple) :

        x = (coord[0] - (self.__plateau.getTilewidth()/2)) / self.__plateau.getTilewidth()

        t1 = coord[1] / (self.__plateau.getTileheight()/2)
        t2 = math.floor(x + t1)
        r = math.floor((math.floor(t1 - x) + t2) / 3) 
        q = math.floor((math.floor(2 * x + 1) + t2) / 3) - math.ceil(r/2)

        return (q,r)

    