import pygame
import json
import os

objets = {"armes": {},
          "equipements": {},
          "ressources": {}}


class Objet:
    def __init__(self, nom: str, image, stackable: int = 1):
        """Un Objet.

        Les différents Objets sont instancié à l'avance dans `Jeu.py` à partir du fichier `objet.json`.

        Attributes
        ----------
        _nom : str
            Le nom de l'objet.
        _image : str
            L'image de l'objet.
        _stackable : int
            La quantité max de l'objet dans un seul `Slot_inventaire`.
        """

        self._nom = nom
        self._image = pygame.image.load(image).convert_alpha()
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


class Arme(Objet):
    def __init__(self, nom: str, image, modDegat, modPrecision):
        """Une arme est un objet avec des attributs et des getter supplémentaire.

        Les différents Objets sont instancié à l'avance dans `Jeu.py` à partir du fichier `objet.json`.

        Attributes
        ----------
        _nom : str
            Le nom de l'objet.
        _image : str
            L'image de l'objet.
        _stackable : int
            La quantité max de l'objet dans un seul `Slot_inventaire`. (toujours égale à 1 dans le cas de l'Arme)
        _modDegat : int
            Modificateur de dégats appliqué sur le personnage lorsque l'arme est équipé par un `Personnage`.
        _modPrecision : int
            Modificateur de précision appliqué sur le personnage lorsque l'arme est équipé par un `Personnage`.
        """

        super(Arme, self).__init__(nom, image)
        self._modDegat = modDegat
        self._modPrecision = modPrecision

    def getModDegat(self):
        """Retourne le modificateur de dégat de l'arme."""

        return self._modDegat

    def getModPrecision(self):
        """Retourne le modificateur de précision de l'arme."""

        return self._modPrecision

class Equipement(Objet):
    def __init__(self, nom: str, image, modVie):
        """Une arme est un objet avec des attributs et des getter supplémentaire.

        Les différents Objets sont instancié à l'avance dans `Jeu.py` à partir du fichier `objet.json`.

        Attributes
        ----------
        _nom : str
            Le nom de l'objet.
        _image : str
            L'image de l'objet.
        _stackable : int
            La quantité max de l'objet dans un seul `Slot_inventaire`. (toujours égale à 1 dans le cas de l'Arme)
        _modVie : int
            Modificateur de vie appliqué sur le personnage lorsque l'arme est équipé par un `Personnage`.
        """

        super(Equipement, self).__init__(nom, image)
        self._modVie = modVie

    def getModVie(self):
        """Retourne le modificateur de vie de l'arme."""

        return self._modVie

def loadAllObjets():
    with open("src/dossierJson/objets.json") as fichier:
        data = json.loads(fichier.read())
        for nom, arme in data["armes"].items():
            if os.path.isfile(arme["image"]):
                objets["armes"][nom] = (Arme(nom, arme["image"], arme["modDegat"], arme["modPrecision"]))
                print(objets["armes"][nom])
            else:
                raise FileNotFoundError("L'image de l'arme " + nom + " est introuvable ...")

        for nom, equipements in data["equipements"].items():
            if os.path.isfile(equipements["image"]):
                objets["equipements"][nom] = (Equipement(nom, equipements["image"], equipements["modVie"]))
                print(objets["equipements"][nom])
            else:
                raise FileNotFoundError("L'image de l'equipement " + nom + " est introuvable ...")

        for nom, ressources in data["ressources"].items():
            if os.path.isfile(equipements["image"]):
                objets["ressources"][nom] = (Objet(nom, ressources["image"], ressources["stackable"]))
                print(objets["ressources"][nom])
            else:
                raise FileNotFoundError("L'image de la ressource " + nom + " est introuvable ...")


