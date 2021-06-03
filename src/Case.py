import Evenement
from random import random
from enum import Enum


class Case:
    def __init__(self, image, typeCase: str, proba: int):  # , evenement):
        # self.__evenement: Evenement = evenement
        self.__proba: float = proba
        self.__typeCase: str = typeCase
        self.__image = image

    def eventSeLance(self) -> bool:
        return self.__proba > random()

    def getTypeCase(self) -> Evenement:
        return self.__typeCase

    def getImage(self):
        return self.__image
