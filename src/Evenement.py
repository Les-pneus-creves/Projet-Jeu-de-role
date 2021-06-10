from abc import ABC, abstractmethod  # module pour classe abstraite
import EquipeDePersonnages


class Evenement(ABC):

    def __init__(self):
        self._enCours: bool = True
        self._victoire = True
        self._texteDescr: str = ""
        self._menu = None

    def getTexteDescr(self):
        return self._texteDescr

    def getMenu(self):
        return self._menu

    def getEnCours(self) -> bool:
        return self._enCours

    def getVictoire(self):
        return self._victoire

    def setEncours(self, boule: bool):
        self._enCours = boule

    @abstractmethod
    def getLoot(self):
        """ Retourne un inventaire qui sera donné au joueur à la fin de l'evenement"""
        pass

    @abstractmethod
    def lancement(self, equipePerso: EquipeDePersonnages) -> None:
        pass

    @abstractmethod
    def creerMenu(self, titre: str, texte: str, image):
        pass
