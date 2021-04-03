import Evenement
from random import random
from enum import Enum

class Case:
    def __init__(self, image, typeCase : str):    # , evenement):
        # self.__evenement: Evenement = evenement
        self.__proba: float = 0.5
        self.__typeCase : str = typeCase
        self.__image = image

    def eventSeLance(self) -> bool:
        return self.proba < random()

    def getEvent(self) -> Evenement:
        return self.__evenement

    def getImage(self):
        return self.__image