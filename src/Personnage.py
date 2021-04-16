import pygame
from typing import Type
from typing import Tuple
import Personnage


class Personnage:

    def __init__(self, nom: str, vie: int, force: int, precision: int, initiative: int, image: str):
        self._nom = nom
        self._vie = vie
        self._force = force
        self._precision = precision
        self._initiative = initiative
       # self._image = pygame.image.load(image)
        self._estVivant = True

    def mourir(self) -> None:
        self._estVivant = False

    def estVivant(self) -> bool:
        return self._estVivant

    def getVie(self) -> int:
        return self._vie

    def getInitiative(self) -> int:
        return self._initiative

    # Retourne un int pour la construction de log
    def prendreDegat(self, degat: int) -> int:
        self._vie = self._vie - degat
        return degat

    def attaquer(self, cible: Personnage) -> Tuple[int, int]:
        return self._force, cible.prendreDegat(self._force)

    def __str__(self):
        print("nom: ", self._nom, " vie: ", self._vie, " bruh")


if __name__ == "__main__" :

    x = Personnage("bob", 18, 10, 10, 1, "bob")
    x.__str__()
    x.prendreDegat(10)
    x.__str__()
    x.prendreDegat("oui")
    x.__str__()