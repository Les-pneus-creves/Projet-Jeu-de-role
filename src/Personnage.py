import pygame
from typing import Type
from typing import Tuple
import random
import Personnage
from Inventaire import Inventaire
from Objet import Objet
from copy import copy

coordInScreen = [0, 830]


class Personnage:

    def __init__(self, nom: str, vie: int, force: int, precision: int, initiative: int, image: str):
        """ Un Personnage a différentes stats

        Parameters
        ----------
        _nom: str
            Nom du personnage
        _vie: int
            Le nombre de point actuel de vie
        _vieMax: int
            La vie maximale du Personnage
        _force: int
            Le nombre de point de dégats de base que le personnage inflige
        _precision: int
            Un chiffre allant representant la chance sur 10 de réussir un coup
        _initiative: int
            Permet de commencer plus tot dans un `Combat`
        _image: pygame.image
            L'image du personnage
        _estVivant: bool
            True: le personnage est vivant. False il est mort.
        _inventaire: `Inventaire`
            L'inventaire du personnage
        _coordInScreen: tuple[int]
            Coordonées pour l'affichage de l'équipe sur la map
        """
        self._nom = nom
        self._vie = vie
        self._vieMax = vie
        self._force = force
        self._precision = precision
        self._initiative = initiative
        if image is not None:
            self._image = pygame.image.load(image).convert()
        self._estVivant = True
        self._inventaire = Inventaire(1, 1, 6)
        self.coordInScreen = copy(coordInScreen)
        coordInScreen[0] += 4 * 60 + 30

    def mourir(self) -> None:
        self._estVivant = False

    def getNom(self) -> str:
        return self._nom

    def estVivant(self) -> bool:
        return self._estVivant

    def getVie(self) -> int:
        return self._vie

    def getInitiative(self) -> int:
        return self._initiative

    def prendreDegat(self, degat: int) -> int:
        """ Methode retirant de la vie au personnage

        Parameters
        ----------
        degat: int
            la quantité de point de vie que le personnage va perdre


        Retourne un int pour la construction de log
        """
        self._vie = self._vie - degat
        if self._vie <= 0:
            self._estVivant = False
        return degat

    def attaquer(self, cible: Personnage) -> int:
        """ Methode appelant la méthode prendrerDegat du Personnage ciblé

        Parameters
        ----------

        Cible: Personnage
            Personnage ciblé

        Retourne un int pour la construction de log au moment du combat

        """

        degat = 0

        if "Kv2v2v2" in cible.getNom():

            if self._inventaire.getArme() is not None:
                if self._inventaire.getArme().getNom() == "Arme_Panzerschreck":   #attention il y a arme_ ...
                    degat = self._force + self._inventaire.getArme().getModDegat()
                else:
                    degat = -1
            else:
                degat = -1

        else:
            if random.randint(1, 10) > self._precision:
                return 0

            if self._inventaire.getArme() is not None:
                degat = self._force + self._inventaire.getArme().getModDegat()
            else:
                degat = self._force

        cible.prendreDegat(degat)

        return degat


    def getInventaire(self):
        return self._inventaire

    def addToInventaire(self, objet: Objet, nombre: int = 1):
        self._inventaire.ajouter(objet, nombre)

    def removeFromInventaire(self, objet: Objet, nombre: int = 1):
        self._inventaire.retirer(objet, nombre)

    def __str__(self) -> str:
        return "nom: " + self._nom + " vie: " + str(self._vie)


    def render(self, window):
        window.blit(pygame.transform.scale(self._image, (60, 60)), self.coordInScreen)
        posx = self.coordInScreen[0] + 90
        posy = self.coordInScreen[1]
        font = pygame.font.Font(pygame.font.match_font(pygame.font.get_default_font()), 30)
        text = font.render(self._nom, True, (255, 255, 255))
        window.blit(text, (posx, posy))
        self._inventaire.render(window, self.coordInScreen[0], self.coordInScreen[1] + 60)

    def isInInventory(self, coord: tuple) -> bool:
        return self.coordInScreen[0] <= coord[0] <= (self.coordInScreen[0] + (4 * 60)) and (self.coordInScreen[1] + 60) <= coord[1] <= (self.coordInScreen[1] + (3 * 60))

    def getObjetByCoord(self, point: tuple):
        if self.isInInventory(point):
            coord = int((point[0] - self.coordInScreen[0]) / 60), int((point[1] - (self.coordInScreen[1] + 60)) / 60)
            index = coord[0] + (coord[1] * 4)
            return self._inventaire[index].getObjet()


if __name__ == "__main__":
    x = Personnage("bob", 18, 10, 10, 1, "bob")
    print(x)
    x.prendreDegat(10)
    print(x)
