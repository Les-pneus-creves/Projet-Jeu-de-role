import Evenement
import math
from PlateauDeJeu import PlateauDeJeu
import pygame
import EquipeDePersonnages
import Objet


class Expedition:

    def __init__(self, equipe, plateau):
        self._temps: int = 1  # Numéro du tour de l'expédition en cour
        self._equipe: EquipeDePersonnages = equipe  # Equipe de personnage joueur du joueur
        self._eventEnCours: Evenement = None  # Even ement actuellement en cours
        self._plateau: PlateauDeJeu = plateau  # Plateau sur lequel l'éxpedition se déroule
        for personnage in self._equipe.getPersonnages():
            personnage.addToInventaire(Objet.objets["armes"]["Arme_Arc"])

    # lecture des evenements
    def on_event(self, event) -> tuple:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Lorsque je clic gauche sur une unite et que j'en ai pas de selectionnée

            x = int(event.pos[0])  # Enregistre la coordonnée y de l'event
            y = int(event.pos[1])  # Enregistre la coordonnée y de l'event
            print("clic :", x, y)

            xInGrid, yInGrid = self.pointToCoord((x, y))

            if self._plateau.isInTheMap((xInGrid, yInGrid)):
                print((xInGrid, yInGrid))
                self._equipe.deplacement((xInGrid, yInGrid))  # Déplacement de l'équipe

                if self._plateau.getCase((xInGrid, yInGrid)).eventSeLance():
                    return xInGrid, yInGrid
                else:
                    return None
            elif self.isInOneInventory((x, y))[0]:
                print(self._equipe.getPersonnages()[self.isInOneInventory((x, y))[1]].getObjetByCoord((x, y)))
            else:
                return None

        else:
            return None

    # Calcul des mises à jours
    def on_loop(self) -> None:
        pass

    # Calcul des affichages
    def on_render(self, window) -> None:
        window.fill((70, 70, 70))
        self._plateau.render(window)
        self._equipe.render(window, (self._plateau.getTilewidth(), self._plateau.getTileheight()))
        self.renderPersonnageInventaire(window)

    # Méthode lançant un événement précis
    def returnTypeCase(self, coord) -> str:
        return self._plateau.getCase(coord).getTypeCase()

    def getEquipe(self):
        return self._equipe

    def pointToCoord(self, coord: tuple):

        x = (coord[0] - (self._plateau.getTilewidth() / 2)) / self._plateau.getTilewidth()

        t1 = coord[1] / (self._plateau.getTileheight() / 2)
        t2 = math.floor(x + t1)
        r = math.floor((math.floor(t1 - x) + t2) / 3)
        q = math.floor((math.floor(2 * x + 1) + t2) / 3) - math.ceil(r / 2)

        return q, r

    def renderPersonnageInventaire(self, window):
        peronnages = self._equipe.getPersonnages()

        for peronnage in peronnages:
            """ Il faudrait aussi afficher ici les noms de chaques personnes devant leur inventaires """
            peronnage.render(window)

    def isInOneInventory(self, coord: tuple):
        peronnages = self._equipe.getPersonnages()
        i = 0
        for peronnage in peronnages:
            if peronnage.isInInventory(coord):
                return True, i
            i += 1
        return False, i
