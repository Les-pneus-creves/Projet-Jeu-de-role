import Evenement
import math
from PlateauDeJeu import PlateauDeJeu
import pygame
import EquipeDePersonnages


class Expedition:

    def __init__(self, equipe, plateau):
        self._temps: int = 1  # Numéro du tour de l'expédition en cour
        self._equipe: EquipeDePersonnages = equipe  # Equipe de personnage joueur du joueur
        self._eventEnCours: Evenement = None  # Even ement actuellement en cours
        self._plateau: PlateauDeJeu = plateau  # Plateau sur lequel l'éxpedition se déroule

    # lecture des evenements
    def on_event(self, event) -> tuple:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Lorsque je clic gauche sur une unite et que j'en ai pas de selectionnée

            xInMap = int(event.pos[0])  # Enregistre la coordonnée y de l'event
            yInMap = int(event.pos[1])  # Enregistre la coordonnée y de l'event
            print("clic :", xInMap, yInMap)

            xInGrid, yInGrid = self.pointToCoord((xInMap, yInMap))
            print((xInGrid, yInGrid))

            if self._plateau.isInTheMap((xInGrid, yInGrid)):
                self._equipe.deplacement((xInGrid, yInGrid))  # Déplacement de l'équipe

                if self._plateau.getCase((xInGrid, yInGrid)).eventSeLance():
                    return xInGrid, yInGrid
                else:
                    return None
            else:
                return None

        else:
            return None

    # Calcul des mises à jours
    def on_loop(self) -> None:
        pass

    # Calcul des affichages
    def on_render(self, window) -> None:
        self._plateau.render(window)
        self._equipe.render(window, (self._plateau.getTilewidth(), self._plateau.getTileheight()))
        self.renderInventaires(window)

    # Méthode permettant de sélectionner aléatoirement (ou non?) un plateau
    def selectPlateau(self) -> None:
        pass

    # Méthode lançant un événement précis
    def returnTypeCase(self, coord) -> str:
        return self._plateau.getCase(coord).getTypeCase()

    # Méthode retournant true ou false selon si des coordonnées (En pixel ou en case/hexagone??) sont effectivement dans la map
    def estDansLaMap(self, coord) -> bool:
        pass

    def pointToCoord(self, coord: tuple):

        x = (coord[0] - (self._plateau.getTilewidth() / 2)) / self._plateau.getTilewidth()

        t1 = coord[1] / (self._plateau.getTileheight() / 2)
        t2 = math.floor(x + t1)
        r = math.floor((math.floor(t1 - x) + t2) / 3)
        q = math.floor((math.floor(2 * x + 1) + t2) / 3) - math.ceil(r / 2)

        return q, r

    def renderInventaires(self, window):
        peronnages = self._equipe.getPersonnages()
        minx = 0
        miny = 830

        for peronnage in peronnages:
            """ Il faudrait aussi afficher ici les noms de chaques personnes devant leur inventaires """
            peronnage.render(window, minx, miny)
            peronnage.getInventaire().render(window, minx, miny + 60)
            minx += 60 * 4 + 30
