from abc import ABC, abstractmethod #module pour classe abstraite
import EquipeDePersonnages

class Evenement(ABC):

    def __init__(self):
        self.__enCours: bool = True
        self.__texteDescr: str = ""

    @abstractmethod
    def lancement(self,equipePerso: EquipeDePersonnages) -> None:
        pass

