import Evenement
import math
from PlateauDeJeu import PlateauDeJeu
import pygame
import EquipeDePersonnages
import Objet


class Expedition:

    def __init__(self, equipe, plateau):
        """ Une expédition !

        Parameters
        ----------
        _temps: int
            Numéro du tour de l'expédition en cour (Non exploité dans la version actuel du jeu)
        _equipe: `EquipeDePersonnages`
            Equipe de personnage joueur du joueur
        _plateau: `PlateauDeJeu`
            Plateau sur lequel l'expédition se déroule
        """
        self._temps: int = 1  # Numéro du tour de l'expédition en cour
        self._equipe: EquipeDePersonnages = equipe  # Equipe de personnage joueur du joueur
        self._plateau: PlateauDeJeu = plateau  # Plateau sur lequel l'éxpedition se déroule
        for personnage in self._equipe.getPersonnages():
            personnage.addToInventaire(Objet.objets["Arc"])

        self.objetSelectione = None

    def on_event(self, event) -> tuple:
        """Lecture des évènements pygame tel les clics"""
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
                personnageSelection = self._equipe.getPersonnages()[self.isInOneInventory((x, y))[1]]
                if self.objetSelectione is None:
                    self.objetSelectione = personnageSelection.getObjetByCoord((x, y))
                    if self.objetSelectione is not None:
                        personnageSelection.removeFromInventaire(self.objetSelectione)
                else:
                    objetDestination = personnageSelection.getObjetByCoord((x, y))
                    if objetDestination is None or objetDestination.getNom() == self._objetSelectione.getNom():
                        personnageSelection.addToInventaire(self.objetSelectione)
                        self.objetSelectione = None
                    else:
                        personnageSelection.removeFromInventaire(objetDestination)
                        personnageSelection.addToInventaire(self.objetSelectione)
                        self.objetSelectione = objetDestination
            else:
                return None

        else:
            return None

    # Calcul des mises à jours
    def on_loop(self) -> None:
        """Calcul des mises à jours du jeu"""
        pass

    # Calcul des affichages
    def on_render(self, window) -> None:
        """Calcul des affichages et affichage sur la fenêtre"""
        window.fill((70, 70, 70))
        self._plateau.render(window)
        self._equipe.render(window, (self._plateau.getTilewidth(), self._plateau.getTileheight()))
        self._equipe.renderPersonnageInventaire(window)

    def returnTypeCase(self, coord) -> str:
        return self._plateau.getCase(coord).getTypeCase()

    def getEquipe(self):
        return self._equipe

    def pointToCoord(self, coord: tuple):
        """Méthode permettant de mettre transformer les coordonnées en pixel en coordonnées sur le plateau"""

        x = (coord[0] - (self._plateau.getTilewidth() / 2)) / self._plateau.getTilewidth()

        t1 = coord[1] / (self._plateau.getTileheight() / 2)
        t2 = math.floor(x + t1)
        r = math.floor((math.floor(t1 - x) + t2) / 3)
        q = math.floor((math.floor(2 * x + 1) + t2) / 3) - math.ceil(r / 2)

        return q, r

    def isInOneInventory(self, coord: tuple):
        """Méthode pour savoir si le clic se trouve dans un `inventaire` et si oui dans lequel"""
        peronnages = self._equipe.getPersonnages()
        i = 0
        for peronnage in peronnages:
            if peronnage.isInInventory(coord):
                return True, i
            i += 1
        return False, i
