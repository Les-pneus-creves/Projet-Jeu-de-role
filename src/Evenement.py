import abc #module pour classe abstraite
import EquipeDePersonnages

class Evenement(metaclass=abc.ABCMeta):

    def __init__(self):
        self.__enCours: bool = True
        self.__texteDescr: str = ""

    @abc.abstractmethod
    def lancement(self,equipePerso: EquipeDePersonnages) -> None:
        pass
