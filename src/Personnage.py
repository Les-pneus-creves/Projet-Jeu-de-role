import pygame
import random
import Personnage
from Inventaire import Inventaire
import Objet
from copy import copy

coordInScreen = [0, 830]
"""Coordonnées où va s'afficher la description du prochain personnage créé."""


class Personnage:

    def __init__(self, nom: str, vie: int, force: int, precision: int, initiative: int, image: str):
        """ Un Personnage a différentes stats

        Attributes
        ----------
        _nom: str
            Nom du personnage
        _vie: int
            Le nombre de point actuel de vie
        _vieMax: int
            La vie maximale du Personnage
        _force: int
            Le nombre de point de dégâts de base que le personnage inflige
        _precision: int
            Un chiffre allant représentant la chance sur 10 de réussir un coup
        _initiative: int
            Permet de commencer plus tot dans un `Combat`
        _image: pygame.image
            L'image du personnage
        _estVivant: bool
            True: le personnage est vivant. False il est mort.
        _inventaire: `src.Inventaire`
            L'inventaire du personnage
        _coordInScreen: tuple[int]
            Coordonnées pour l'affichage de la description du personnage
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
        self._vie = 0

    def getNom(self) -> str:
        return self._nom

    def estVivant(self) -> bool:
        return self._estVivant

    def getVie(self) -> int:
        return self._vie

    def getInitiative(self) -> int:
        return self._initiative

    def soigner(self, soin: int):
        if self._estVivant:
            self._vie += soin

    def prendreDegat(self, degat: int) -> int:
        """ Methode retirant de la vie au personnage

        Parameters
        ----------
        degat: int
            la quantité de point de vie que le personnage va perdre


        Retourne un int pour la construction de log
        """
        if self._inventaire.getEquipement() is not None:
            degatReduit = degat-self._inventaire.getEquipement().getModDegat()
            if degatReduit < 0:
                degatReduit = 0
        else:
            degatReduit = degat

        self._vie = self._vie - degatReduit
        if self._vie <= 0:
            self.mourir()
        return degatReduit

    def attaquer(self, cible: Personnage) -> int:
        """ Methode appelant la méthode prendrerDegat du Personnage ciblé

        Parameters
        ----------
        cible: Personnage
            Personnage ciblé

        Retourne un int pour la construction de log au moment du combat

        """

        degat = 0

        if "Kv2v2v2" in cible.getNom():

            if self._inventaire.getArme() is not None:
                if self._inventaire.getArme().getNom() == "Panzerschreck":   #attention il y a arme_ ...
                    degat = self._force + self._inventaire.getArme().getModDegat()
                else:
                    degat = -1
            else:
                degat = -1

        else:
            if self._inventaire.getArme() is not None:
                if random.randint(1, 10) > self._precision+self._inventaire.getArme().getModPrecision():
                    return 0
            else:
                if random.randint(1, 10) > self._precision:
                    return 0

            if self._inventaire.getArme() is not None:
                degat = self._force + self._inventaire.getArme().getModDegat()
            else:
                degat = self._force

        cible.prendreDegat(degat)

        return degat


    def getInventaire(self) -> Inventaire:
        return self._inventaire

    def addToInventaire(self, objet: Objet, nombre: int = 1):
        self._inventaire.ajouter(objet, nombre)

    def removeFromInventaire(self, objet: Objet, nombre: int = 1):
        self._inventaire.retirer(objet, nombre)

    def __str__(self) -> str:
        return "nom: " + self._nom + " vie: " + str(self._vie)


    def render(self, window):
        pygame.draw.rect(window, (5, 5, 5), (self.coordInScreen[0], self.coordInScreen[1], 240, 180), border_radius=5)
        window.blit(pygame.transform.scale(self._image, (60, 60)), self.coordInScreen)
        posx = self.coordInScreen[0] + 80
        posy = self.coordInScreen[1] + 5
        font = pygame.font.Font(pygame.font.match_font(pygame.font.get_default_font()), 30)
        text = font.render(self._nom, True, (255, 255, 255))
        window.blit(text, (posx, posy))
        posy += 30
        text = font.render("Vie : " + str(self._vie), True, (255, 255, 255))
        window.blit(text, (posx, posy))

        self._inventaire.render(window, self.coordInScreen[0], self.coordInScreen[1] + 60)

    def isInInventory(self, coord: tuple) -> bool:
        """Retourne `True` si les coordonnées donné en paramètres sont dans la zone d'affichage de l'inventaire du personnage

        Retourne `False` sinon
        """
        return self.coordInScreen[0] <= coord[0] <= (self.coordInScreen[0] + (4 * 60)) and (self.coordInScreen[1] + 60) <= coord[1] <= (self.coordInScreen[1] + (3 * 60))

    def getObjetByCoord(self, point: tuple) -> Objet:
        """Retourne l'objet sur lequel on a cliqué"""
        if self.isInInventory(point):
            coord = int((point[0] - self.coordInScreen[0]) / 60), int((point[1] - (self.coordInScreen[1] + 60)) / 60)
            index = coord[0] + (coord[1] * 4)
            return self._inventaire[index].getObjet()
        return None

    def nbDePatate(self):
        patate = 0
        for slot in self._inventaire.slotsOfThisObjet(Objet.objets["Patate"]):
            patate += self._inventaire[slot].getNbContenue()
        return patate

if __name__ == "__main__":
    x = Personnage("bob", 18, 10, 10, 1, "bob")
    print(x)
    x.prendreDegat(10)
    print(x)
