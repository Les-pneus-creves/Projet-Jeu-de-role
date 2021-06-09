import Evenement
from random import random
from enum import Enum


class Case:
    def __init__(self, image, typeCase: str, proba: int):  # , evenement):
        """ Un case a une image pour s'afficher, un type et une probabilité d'evenement.

        Parameters
        ----------
        image : pygame.image
            Image de la case
        typeCase : str
            Type de la case
        proba : int
            Probabilité d'avoir un évènement qui se lance quand l'équipe se déplace sur ce type de case
                        """
        self.__proba: float = proba
        self.__typeCase: str = typeCase
        self.__image = image

    def eventSeLance(self) -> bool:
        """ Méthode renvoyant true si l'évènement de la case se lance

        Retourne un booléen: True si l'évènement se lance, False sinon
        """
        return self.__proba > random()

    def getTypeCase(self) -> Evenement:
        return self.__typeCase

    def getImage(self):
        return self.__image
