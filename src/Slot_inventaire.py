import Objet
import pygame

typeObjetImages = {}
"""Liste des images pour chaque types de slots."""


class Slot_inventaire:
    def __init__(self, typeObjet: str):
        """Un slot inventaire permet de stocké un type d'objet bien particulier précisé lors de l'instanciation du slot.

        Attributes
        ----------
        _objet : Objet
            L'objet contenue dans le slot.
        _typeObjet : str
            Le type d'objet que peut contenir le slot.
        _nbContenur : int
            La quantité de l'objet dans le slot.
        """
        self._objet = None
        self._typeObjet = typeObjet
        self._nbContenue = 0
        loadSlotsImages()
        # Il faut que je fasse en sorte qu eça s'execute qu'une seul fois.

    def __str__(self):
        return "[" + str(self._objet) + ", " + self._typeObjet + ", " + str(self._nbContenue) + "]"

    def vider(self):
        """Permet de vide totalement le slot."""
        self._nbContenue = 0
        self._objet = None

    def ajouter(self, objet: Objet = None, nombre: int = 1):
        """Ajoute dans le slot l'objet donné en paramètre autant de fois que précisé (par défaut 1 seul) et
        s'il n'y a pas assez de place retourne le nombre d'objet qu'il n'a pas peu ajouter dans ce slot.

        Si l'objet ne peut pas être ajouté dans le slot la méthode retourne `-1`.
        """

        if objet is None and self._objet is not None:
            objet = self._objet

        if self.puisJeAjouter(objet):
            self._objet: Objet = objet
            if not self.plein():
                if self._nbContenue + nombre > self._objet.getStackable():
                    nombre -= self._objet.getStackable() - self._nbContenue
                    self._nbContenue = self._objet.getStackable()
                    return nombre
                else:
                    self._nbContenue += nombre
                    return 0
        return -1

    def retirer(self, nombre: int = 1):
        """Retire du slot l'objet donné en paramètre autant de fois que précisé (par défaut 1 seul) et
        s'il n'y a pas assez d'objet à retirer retourne le nombre d'objet qu'il n'a pas peu retirer du slot.
        """

        self._nbContenue -= nombre
        if self._nbContenue <= 0:
            nb = self._nbContenue
            self.vider()
            return nb
        else:
            return 0

    def puisJeAjouter(self, objet):
        """Vérifie si on peut ajouter l'objet donné en paramètre dans ce slot."""

        if objet is not None:
            if self._objet is None:
                return isinstance(objet, self._typeObjet) or self._typeObjet == "Ressources"
            else:
                return objet.getNom() == self._objet.getNom()
        return False

    def getObjet(self):
        """Retourne l'objet contenue dans le slot (`None` si le slot est vide)."""

        if not self.vide():
            return self._objet
        return None

    def vide(self):
        """Retourne `True` si le slot est vide et `False` sinon."""

        return self._nbContenue == 0 and self._objet is None

    def plein(self):
        """Retourne `True` si le slot est plein et `False` sinon."""

        return self._nbContenue == self._objet.getStackable()

    def getNbContenue(self):
        """Retourne la quantité de l'objet contenue dans le slot (`0` si le slot est vide)."""

        return self._nbContenue

    def getTypeObjet(self):
        """Retourne le type d'objet que peut contenir le slot"""

        return self._typeObjet

    def render(self, window, posx, posy):
        """Permet d'afficher le slot dans une fenêtre pygame à une position donné.

        Parameters
        ----------
        window : pygame.Surface
            La fenêtre sur laquelle on veut afficher l'inventaire.
        posx : int
            Position x (en pixel) à partir de laquelle l'inventaire sera affiché sur la fenêtre.
        posy : int
            Position y (en pixel) à partir de laquelle l'inventaire sera affiché sur la fenêtre.
        """
        if self.vide():
            window.blit(pygame.transform.scale(typeObjetImages[self._typeObjet], (60, 60)), (posx, posy))
        else:
            window.blit(pygame.transform.scale(typeObjetImages[Objet.Objet], (60, 60)), (posx, posy))
            window.blit(pygame.transform.scale(self._objet.getImage(), (60, 60)), (posx, posy))


def loadSlotsImages():
    """Fonction chargeant les images pour chaque type de slots dans la variable globale `typeObjetImages`."""

    global typeObjetImages
    typeObjetImages = {Objet.Arme: pygame.image.load("src/images/Inventory/Slot_arme.png").convert(),
                       Objet.Equipement: pygame.image.load("src/images/Inventory/Slot_equipement.png").convert(),
                       Objet.Objet: pygame.image.load("src/images/Inventory/Slot_ressources.png").convert(),
                       "Selection": pygame.image.load("src/images/Inventory/Slot_select.png").convert()}
