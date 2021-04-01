import Evenement
import random
from enum import Enum

class Case:
    def __init__(self, image, typeCase):    # , evenement):
        # self.__evenement: Evenement = evenement
        self.__proba: float = 0.5
        self.__typeCase = typeCase
        self.__image = image

    def eventSeLance(self) -> bool:
        return self.proba < random.random()

    def getEvent(self) -> Evenement:
        return self.__evenement

    def getImage(self):
        return self.__image