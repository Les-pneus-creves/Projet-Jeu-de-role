import pygame


class Objet:
    def __init__(self, nom: str, image, stackable: int = 1):
        """Un Objet.

        Les différents Objets sont instancié à l'avance dans `Jeu.py` à partir du fichier `objet.json`.

        Attributes
        ----------
        _nom : str
            L'objet contenue dans le slot.
        _image : str
            Le type d'objet que peut contenir le slot.
        _stackable : int
            La quantité de l'objet dans le slot.
        """

        self._nom = nom
        self._image = pygame.image.load(image).convert()
        self._stackable = stackable

    def __str__(self):
        return "[" + self._nom + ", max= " + str(self._stackable) + "]"

    def getImage(self):
        """Retourne l'image sous forme d'objet pygame prêt à être affiché"""
        return self._image

    def getNom(self) -> str:
        """Retourne le nom de l'objet en `str`"""
        return self._nom

    def getStackable(self) -> int:
        """Retourne le nombre de fois ou on peut mettre cette objet dans un seul slot inventaire"""
        return self._stackable
