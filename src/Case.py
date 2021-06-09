import Evenement
from random import random
from enum import Enum


class Case:
    def __init__(self, image, typeCase: str, proba: int):  # , evenement):
        """ Un case a une iamge pour s'afficher, un type et une probabilité d'evenement.

        Parameters
        ----------
        image : pygame.image
            image de la case
        typeCase : str
            Type de la case
        proba : int
            probabilité d'avoir un evenement qui se lance quand l'équipe se déplace sur ce type de case
                        """
        # self.__evenement: Evenement = evenement
        self.__proba: float = proba
        self.__typeCase: str = typeCase
        self.__image = image

    def eventSeLance(self) -> bool:
        """ Méthode renvoyant true si l'évenement de la case se lance

        retourne un booléen: True si l'evenement se lance, False sinon
        """
        return self.__proba > random()

    def getTypeCase(self) -> Evenement:
        return self.__typeCase

    def getImage(self):
        return self.__image
