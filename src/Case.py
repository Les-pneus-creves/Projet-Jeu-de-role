import Evenement
import random
from enum import Enum

TypeCase = Enum('TypeCase', 'HERBE TERRE EAU NEIGE')

class Case:
    def __init__(self, typeCase, evenement):
        self.__evenement: Evenement = evenement
        self.__proba: float = 0.5
        self.__typeCase: TypeCase = typeCase 

    def eventSeLance(self) -> bool:
        return self.proba < random.random()

    def getEvent(self) -> Evenement:
        return self.__evenement