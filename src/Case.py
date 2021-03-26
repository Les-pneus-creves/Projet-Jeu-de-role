import Evenement
import random
from enum import Enum

TypeCase = Enum('TypeCase', 'HERBE TERRE EAU NEIGE')

class TypeCase(Enum):
    HERBE = 50
    TERRE = 26
    EAU = 2
    NEIGE = 25
    VIDE = 69
    AUTOROUTEHGBD = 23
    JSP = 14
    JSP2 = 16
    CAMIONTERRE = 43
    CAMIONSOIN = 67
    ETANG = 37
    ROCHER = 60

class Case:
    def __init__(self, image, typeCase):    # , evenement):
        # self.__evenement: Evenement = evenement
        self.__proba: float = 0.5
        self.__typeCase: TypeCase = TypeCase(typeCase) 
        self.__image = image

    def eventSeLance(self) -> bool:
        return self.proba < random.random()

    def getEvent(self) -> Evenement:
        return self.__evenement

    def getImage(self):
        return self.__image