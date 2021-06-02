import pygame
from typing import Type
from typing import Tuple
import random
import Personnage
from Inventaire import Inventaire


class Personnage:

    def __init__(self, nom: str, vie: int, force: int, precision: int, initiative: int, image: str):
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

    # Retourne un int pour la construction de log
    def prendreDegat(self, degat: int) -> int:
        self._vie = self._vie - degat
        if self._vie <= 0:
            self._estVivant = False
        return degat

    def attaquer(self, cible: Personnage) -> int:

        if random.randint(1, 10) > self._initiative:
            return 0

        else:
            if self._inventaire.getArme() is not None:
                degat = self._force + self._inventaire.getArme().getModDegat()
            else:
                degat = self._force

        cible.prendreDegat(degat)

        return degat

    def getInventaire(self):
        return self._inventaire

    def __str__(self) -> str:
        return "nom: " + self._nom + " vie: " + str(self._vie)

    def render(self, window, minx, miny):
        posx = minx
        posy = miny
        window.blit(pygame.transform.scale(self._image, (60, 60)), (posx, posy))
        posx += 90
        font = pygame.font.Font(pygame.font.match_font(pygame.font.get_default_font()), 30)
        text = font.render(self._nom, True, (255, 255, 255))
        window.blit(text, (posx, posy))


if __name__ == "__main__":
    x = Personnage("bob", 18, 10, 10, 1, "bob")
    print(x)
    x.prendreDegat(10)
    print(x)
