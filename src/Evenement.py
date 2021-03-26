from abc import ABC, abstractmethod #module pour classe abstraite
import EquipeDePersonnages

class Evenement(ABC):

    def __init__(self):
        self.__enCours: bool = True
        self.__texteDescr: str = ""
        self.__menu = None

    #Faut faire comme ça pour une propriété abstraite
    @property
    @abstractmethod
    def texteDescr(self):
        pass

    @texteDescr.setter
    @abstractmethod
    def texteDescr(self, value):
        pass

    @property
    @abstractmethod
    def menu(self):
        pass

    @menu.setter
    @abstractmethod
    def menu(self, value):
        pass

    @abstractmethod
    def lancement(self,equipePerso: EquipeDePersonnages) -> None:
        pass

    @abstractmethod
    def creerMenu(self, titre: str, texte : str, image):
        pass
